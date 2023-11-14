# GridCal
# Copyright (C) 2015 - 2023 Santiago Peñate Vera
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 3 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
import numpy as np
import time
from typing import Union
from GridCalEngine.Core.Devices.multi_circuit import MultiCircuit
from GridCalEngine.basic_structures import SolverType
from GridCalEngine.Simulations.OPF.opf_options import OptimalPowerFlowOptions
from GridCalEngine.Simulations.OPF.linear_opf_ts import run_linear_opf_ts
from GridCalEngine.Simulations.OPF.simple_dispatch_ts import run_simple_dispatch
from GridCalEngine.Simulations.OPF.opf_results import OptimalPowerFlowResults
from GridCalEngine.Simulations.driver_types import SimulationTypes
from GridCalEngine.Simulations.PowerFlow.power_flow_options import PowerFlowOptions
from GridCalEngine.Simulations.driver_template import TimeSeriesDriverTemplate
from GridCalEngine.Core.Compilers.circuit_to_newton_pa import newton_pa_linear_opf, newton_pa_nonlinear_opf
import GridCalEngine.basic_structures as bs


class OptimalPowerFlowDriver(TimeSeriesDriverTemplate):
    name = 'Optimal power flow'
    tpe = SimulationTypes.OPF_run

    def __init__(self,
                 grid: MultiCircuit,
                 options: Union[OptimalPowerFlowOptions, None] = None,
                 engine: bs.EngineType = bs.EngineType.GridCal):
        """
        PowerFlowDriver class constructor
        :param grid: MultiCircuit Object
        :param options: OPF options
        :param engine: Calculation engine to use (if available)
        """
        TimeSeriesDriverTemplate.__init__(self,
                                          grid=grid,
                                          time_indices=None,
                                          clustering_results=None,
                                          engine=engine,
                                          check_time_series=False)

        # Options to use
        self.options = options if options else OptimalPowerFlowOptions()

        F, T = self.grid.get_branch_number_wo_hvdc_FT()
        F_hvdc, T_hvdc = self.grid.get_hvdc_FT()

        # OPF results
        self.results: OptimalPowerFlowResults = OptimalPowerFlowResults(
            bus_names=self.grid.get_bus_names(),
            branch_names=self.grid.get_branch_names_wo_hvdc(),
            load_names=self.grid.get_load_names(),
            generator_names=self.grid.get_generator_names(),
            battery_names=self.grid.get_battery_names(),
            hvdc_names=self.grid.get_hvdc_names(),
            bus_types=np.ones(self.grid.get_bus_number(), dtype=int),
            area_names=self.grid.get_area_names(),
            F=F,
            T=T,
            F_hvdc=F_hvdc,
            T_hvdc=T_hvdc,
            bus_area_indices=self.grid.get_bus_area_indices()
        )

        self.all_solved = True

    @property
    def pf_options(self) -> PowerFlowOptions:
        """
        Get the PowerFlow options provides with the OpfOptions
        :return: PowerFlowOptions
        """
        return self.options.power_flow_options

    def get_steps(self):
        """
        Get time steps list of strings
        """
        return []

    def add_report(self):
        """
        Add a report of the results (in-place)
        """

        for gen_name, gen_shedding in zip(self.results.generator_names, self.results.generator_shedding):
            if gen_shedding > 0:
                self.logger.add_warning("Generation shedding",
                                        device=gen_name,
                                        value=gen_shedding,
                                        expected_value=0.0)

        for load_name, load_shedding in zip(self.results.load_names, self.results.load_shedding):
            if load_shedding > 0:
                self.logger.add_warning("Load shedding",
                                        device=load_name,
                                        value=load_shedding,
                                        expected_value=0.0)

        for name, val in zip(self.results.branch_names, self.results.loading):
            if val > 1:
                self.logger.add_warning("Overload",
                                        device=name,
                                        value=val * 100,
                                        expected_value=100.0)

        va = np.angle(self.results.voltage)
        for i, bus in enumerate(self.grid.buses):
            if va[i] > bus.angle_max:
                self.logger.add_warning("Overvoltage",
                                        device=bus.name,
                                        value=va[i],
                                        expected_value=bus.angle_max)
            elif va[i] < bus.angle_min:
                self.logger.add_warning("Undervoltage",
                                        device=bus.name,
                                        value=va[i],
                                        expected_value=bus.angle_min)

    def opf(self, remote=False, batteries_energy_0=None):
        """
        Run a power flow for every circuit
        :param remote: is this function being called from the time series?
        :param batteries_energy_0: initial state of the batteries, if None the default values are taken
        :return: OptimalPowerFlowResults object
        """

        if not remote:
            self.progress_signal.emit(0.0)
            self.progress_text.emit('Formulating problem...')

        if self.options.solver == SolverType.DC_OPF:

            # DC optimal power flow
            opf_vars = run_linear_opf_ts(grid=self.grid,
                                         time_indices=None,
                                         solver_type=self.options.mip_solver,
                                         zonal_grouping=self.options.zonal_grouping,
                                         skip_generation_limits=self.options.skip_generation_limits,
                                         consider_contingencies=self.options.consider_contingencies,
                                         lodf_threshold=self.options.lodf_tolerance,
                                         maximize_inter_area_flow=self.options.maximize_flows,
                                         buses_areas_1=self.options.area_from_bus_idx,
                                         buses_areas_2=self.options.area_to_bus_idx,
                                         energy_0=None,
                                         logger=self.logger,
                                         export_model_fname=self.options.export_model_fname)

            self.results.voltage = np.ones(opf_vars.nbus) * np.exp(1j * opf_vars.bus_vars.theta[0, :])
            self.results.bus_shadow_prices = opf_vars.bus_vars.shadow_prices[0, :]
            self.results.load_shedding = opf_vars.load_vars.shedding[0, :]
            self.results.battery_power = opf_vars.batt_vars.p[0, :]
            # self.results.battery_energy = opf_vars.batt_vars.e[0, :]
            self.results.generator_power = opf_vars.gen_vars.p[0, :]
            self.results.Sf = opf_vars.branch_vars.flows[0, :]
            self.results.St = -opf_vars.branch_vars.flows[0, :]
            self.results.overloads = opf_vars.branch_vars.flow_slacks_pos[0, :] - opf_vars.branch_vars.flow_slacks_neg[
                                                                                  0, :]
            self.results.loading = opf_vars.branch_vars.loading[0, :]
            self.results.phase_shift = opf_vars.branch_vars.tap_angles[0, :]
            # self.results.Sbus = problem.get_power_injections()[0, :]
            self.results.hvdc_Pf = opf_vars.hvdc_vars.flows[0, :]
            self.results.hvdc_loading = opf_vars.hvdc_vars.loading[0, :]
            self.results.converged = opf_vars.acceptable_solution

        elif self.options.solver == SolverType.Simple_OPF:

            # AC optimal power flow
            Pl, Pg = run_simple_dispatch(grid=self.grid,
                                         text_prog=self.progress_text.emit,
                                         prog_func=self.progress_signal.emit)

            self.results.generator_power = Pg

        else:
            self.logger.add_error('Solver not supported in this mode', str(self.options.solver))
            return

        if not remote:
            self.progress_signal.emit(0.0)
            self.progress_text.emit('Running all in an external solver, this may take a while...')

        # self.results.contingency_flows_list += problem.get_contingency_flows_list().tolist()
        # self.results.contingency_indices_list += problem.contingency_indices_list
        # self.results.contingency_flows_slacks_list += problem.get_contingency_flows_slacks_list().tolist()

        return self.results

    def run(self):
        """

        :return:
        """

        self.tic()
        if self.engine == bs.EngineType.GridCal:

            self.opf()

        elif self.engine == bs.EngineType.NewtonPA:

            ti = self.time_indices if self.time_indices is not None else 0
            use_time_series = self.time_indices is not None

            if self.options.solver == SolverType.DC_OPF:
                self.progress_text.emit('Running Linear OPF with Newton...')

                npa_res = newton_pa_linear_opf(circuit=self.grid,
                                               opf_options=self.options,
                                               pf_opt=PowerFlowOptions(),
                                               time_series=use_time_series,
                                               time_indices=self.time_indices)

                self.results.voltage = npa_res.voltage_module[0, :] * np.exp(1j * npa_res.voltage_angle[0, :])
                self.results.bus_shadow_prices = npa_res.nodal_shadow_prices[0, :]
                self.results.load_shedding = npa_res.load_shedding[0, :]
                self.results.battery_power = npa_res.battery_power[0, :]
                # self.results.battery_energy = npa_res.battery_energy[0, :]
                self.results.generator_power = npa_res.generator_power[0, :]
                self.results.Sf = npa_res.branch_flows[0, :]
                self.results.St = -npa_res.branch_flows[0, :]
                self.results.overloads = npa_res.branch_overloads[0, :]
                self.results.loading = npa_res.branch_loading[0, :]
                self.results.phase_shift = npa_res.branch_tap_angle[0, :]

                # self.results.Sbus = npa_res.
                self.results.hvdc_Pf = npa_res.hvdc_flows[0, :]
                self.results.hvdc_loading = npa_res.hvdc_loading[0, :]
                self.results.converged = True

            if self.options.solver == SolverType.AC_OPF:
                self.progress_text.emit('Running Non-Linear OPF with Newton...')

                # pack the results
                npa_res = newton_pa_nonlinear_opf(circuit=self.grid,
                                                  pf_opt=self.pf_options,
                                                  opf_opt=self.options,
                                                  time_series=use_time_series,
                                                  time_indices=self.time_indices)

                self.results.voltage = npa_res.voltage[0, :]
                self.results.Sbus = npa_res.Scalc[0, :]
                self.results.bus_shadow_prices = npa_res.bus_shadow_prices[0, :]
                self.results.load_shedding = npa_res.load_shedding[0, :]
                self.results.battery_power = npa_res.battery_p[0, :]
                # self.results.battery_energy = npa_res.battery_energy[0, :]
                self.results.generator_power = npa_res.generator_p[0, :]
                self.results.Sf = npa_res.Sf[0, :]
                self.results.St = npa_res.St[0, :]
                self.results.overloads = npa_res.branch_overload[0, :]
                self.results.loading = npa_res.Loading[0, :]
                self.results.phase_shift = npa_res.tap_angle[0, :]

                self.results.hvdc_Pf = npa_res.hvdc_Pf[0, :]
                self.results.hvdc_loading = npa_res.hvdc_loading[0, :]
                self.results.converged = npa_res.converged

        self.toc()

        if self.options.generate_report:
            self.add_report()
