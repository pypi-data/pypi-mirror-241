"""Several ui layout components."""

import os
import csv

# Import Kivy modules
from kivy.properties import ObjectProperty  # pylint: disable=no-name-in-module
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.tabbedpanel import TabbedPanel

# Import the plotting functionalities
from .plot import BuzzPlot
from .output import settings_data_rows
from ..util.settingsparser import SettingsParser

LINE_TYPES = {
    "ac_r": "AC R",
    "ac_s": "AC S",
    "ac_t": "AC T",
    "dc_pos": "DC +",
    "dc_neg": "DC -",
    "dc_neut": "DC Neutral",
    "gnd": "GND",
}


class TableHeaderLabel(Label):
    """TableHeaderLabel is a special Label with border that is used in the
    TableLayout instance for the table headers. The implementation of this
    class can be found in the buzz.kv file.
    """


class TableContentLabel(Label):
    """TableContentLabel is a special Label with border that is used in the
    TableLayout instance for the table contents. The implementation of this
    class can be found in the buzz.kv file.
    """


class TableLayout(GridLayout):
    """TableLayout contains the electric field and audible noise level
    information which complements the audible noise plot. The information shown
    on the table is:

    * line type
    * line coordinates [m]
    * average maximum AC bundle electric field [kV/cm]
    * average maximum DC bundle electric field [kV/cm]
    * audible noise power level [W/m]

    initialization variable(s):

    * tower: Tower instance which holds the electric field and audible noise
            information

    The table is created with the RecycleView class from the Kivy module. The
    implementation of the layout can be found in the buzz.kv file.
    """

    def __init__(self, tower, **kwargs):
        super().__init__(**kwargs)
        self.settings = SettingsParser()

        # Tower instance which holds the electric field and audible noise info
        self.tower = tower

        # Get correct AN unit
        an_unit_string = self.settings.get_an_unit()
        if an_unit_string == "dB over 1pW/m":
            an_string = "dB/pW"
        elif an_unit_string == "dB over 1W/m":
            an_string = "dB/W"
        else:
            an_string = "dB/W"

        # initialize the table headers
        self.headers = [
            "Line",
            "X [m]",
            "Y [m]",
            "AC E-Field [kV/cm]",
            "DC E-Field [kV/cm]",
            "AC EPRI [" + an_string + "]",
            "AC BPA [" + an_string + "]",
            "DC EPRI [" + an_string + "]",
            "DC BPA [" + an_string + "]",
            "DC CRIEPI [" + an_string + "]",
        ]
        for header in self.headers:
            self.add_widget(TableHeaderLabel(text=header))

    def update_table(self):
        """This method updates the table entry after recalculation."""

        # clear the GridLayout
        self.clear_widgets()

        # update the RecycleView data
        self.settings = SettingsParser()
        an_unit_string = self.settings.get_an_unit()
        if an_unit_string == "dB over 1pW/m":
            an_string = "dB/pW"
        elif an_unit_string == "dB over 1W/m":
            an_string = "dB/W"
        else:
            an_string = "dB/W"
        self.headers = [
            "Line",
            "X [m]",
            "Y [m]",
            "AC E-Field [kV/cm]",
            "DC E-Field [kV/cm]",
            "AC EPRI [" + an_string + "]",
            "AC BPA [" + an_string + "]",
            "DC EPRI [" + an_string + "]",
            "DC BPA [" + an_string + "]",
            "DC CRIEPI [" + an_string + "]",
        ]
        for header in self.headers:
            self.add_widget(TableHeaderLabel(text=header))
        entries = self.get_table_data()
        for entry in entries:
            self.add_widget(TableContentLabel(text=entry))

    def get_table_data(self):
        """This method creates the table entry data."""

        an_unit_string = self.settings.get_an_unit()
        unit_conversion = 120 if an_unit_string == "dB over 1pW/m" else 0

        entries = []
        for system in self.tower.systems:
            for line in system.lines:
                # get line type
                entries.append(LINE_TYPES[line.line_type])
                # get line coordinates
                entries.append(str(line.line_x))
                entries.append(str(line.line_y))
                # get the average maximum electric fields
                try:
                    entries.append(f"{line.E_ac:.2f}")
                    entries.append(f"{line.E_dc:.2f}")
                except AttributeError:
                    entries.extend(["", ""])
                try:
                    entries.append(f"{line.AC_EPRI_L_w50 + unit_conversion:.2f}")
                    entries.append(f"{line.AC_BPA_L_w50 + unit_conversion:.2f}")
                except AttributeError:
                    entries.extend(["", ""])
                try:
                    entries.append(f"{line.DC_EPRI_L_w50 + unit_conversion:.2f}")
                    entries.append(f"{line.DC_BPA_L_w50 + unit_conversion:.2f}")
                    entries.append(f"{line.DC_CRIEPI_L_w50 + unit_conversion:.2f}")
                except AttributeError:
                    entries.extend(["", "", ""])
        return entries


class AudibleNoisePlotLayout(BoxLayout):
    """AudibleNoisePlotLayout contains a BuzzPlot instance which is used to
    present the audible noise and tower geometry plots.

    initialization variable(s):

    * tower: Tower instance which calculates the audible noise levels
    """

    def __init__(self, tower, **kwargs):
        super().__init__(**kwargs)

        # Tower instance which calculates the audible noise levels
        self.tower = tower

        # create a BuzzPlot instance and adds it to the layout
        self.plot = BuzzPlot(tower)
        self.add_widget(self.plot)

    def plot_audible_noise(self):
        """This method prompts the BuzzPlot instance to refresh the tower
        geometry and audible noise plots if there are one or more systems in
        the tower instance or clear the plots else.
        """
        if len(self.tower.systems) > 0:
            self.plot.plot_tower_geometry()
            self.plot.plot_audible_noise()
        else:
            self.plot.plot_clear()

    def export_canvas_to_png(self, path, filename):
        """This method prompts the Buzzplot instance to save the plot as a PNG
        image file with the path and filename specified.
        """
        self.plot.export_canvas_to_png(path, filename)

    def reset_settings_parser(self):
        """This method prompts the settings parser belonging to the plot to
        reload configurations from the buzz.ini file"""
        self.plot.reset_settings_parser()


class ElectricFieldPlotLayout(BoxLayout):
    """ElectricFieldPlotLayout contains a BuzzPlot instance which is used to
    present the electric field and tower geometry plots.

    initialization variable(s):

    * tower: Tower instance which calculates the electric field
    """

    def __init__(self, tower, **kwargs):
        super().__init__(**kwargs)

        # Tower instance which calculates the audible noise levels
        self.tower = tower

        # create a BuzzPlot instance and adds it to the layout
        self.plot = BuzzPlot(tower)
        self.add_widget(self.plot)

    def plot_electric_field(self):
        """This method prompts the BuzzPlot instance to refresh the tower
        geometry and electric field plots if there are one or more systems in
        the tower instance or clear the plots else.
        """
        if len(self.tower.systems) > 0:
            self.plot.plot_tower_geometry()
            self.plot.plot_electric_field()
        else:
            self.plot.plot_clear()

    def export_canvas_to_png(self, path, filename):
        """This method prompts the Buzzplot instance to save the plot as a PNG
        image file with the path and filename specified.
        """
        self.plot.export_canvas_to_png(path, filename)

    def reset_settings_parser(self):
        """This method prompts the settings parser belonging to the plot to
        reload configurations from the buzz.ini file"""
        self.plot.reset_settings_parser()


class MagneticFieldPlotLayout(BoxLayout):
    """MagneticFieldPlotLayout contains a BuzzPlot instance which is used to
    present the magnetic field and tower geometry plots.

    initialization variable(s):

    * tower: Tower instance which calculates the magnetic field
    """

    def __init__(self, tower, **kwargs):
        super().__init__(**kwargs)

        # Tower instance which calculates the audible noise levels
        self.tower = tower

        # create a BuzzPlot instance and adds it to the layout
        self.plot = BuzzPlot(tower)
        self.add_widget(self.plot)

    def plot_magnetic_field(self):
        """This method prompts the BuzzPlot instance to refresh the tower
        geometry and magnetic field plots if there are one or more systems in
        the tower instance or clear the plots else.
        """
        if len(self.tower.systems) > 0:
            self.plot.plot_tower_geometry()
            self.plot.plot_magnetic_field()
        else:
            self.plot.plot_clear()

    def export_canvas_to_png(self, path, filename):
        """This method prompts the Buzzplot instance to save the plot as a PNG
        image file with the path and filename specified.
        """
        self.plot.export_canvas_to_png(path, filename)

    def reset_settings_parser(self):
        """This method prompts the settings parser belonging to the plot to
        reload configurations from the buzz.ini file"""
        self.plot.reset_settings_parser()


class DataTabbedPanel(TabbedPanel):
    """DataTabbedPanel inherits from the Kivy TabbedPanel class and contains
    the TableLayout, AudibleNoisePlotLayout, ElectricFieldPlotLayout and
    MagneticFieldPlotLayout instances and present them in different tabs. Users
    can select which plots or table they are willing to see by clicking on the
    tabs. The active tab is shown with a blue bottom border.

    initialization variable(s):

    * tower: Tower instance which calculates the plot data

    The implementation of the layout can be found in the buzz.kv file.
    """

    audible_noise = ObjectProperty(None)
    table = ObjectProperty(None)
    electric_field = ObjectProperty(None)
    magnetic_field = ObjectProperty(None)

    def __init__(self, tower, **kwargs):
        super().__init__(**kwargs)

        # the Tower instance which calculates the plot data
        self.tower = tower

        # create an AudibleNoisePlotLayout instance and adds it to the layout
        self.audible_noise_plot = AudibleNoisePlotLayout(tower)
        self.audible_noise.add_widget(self.audible_noise_plot)

        # create an TableLayout instance and adds it to the layout
        self.table_layout = TableLayout(tower)
        self.table.add_widget(self.table_layout)

        # create an ElectricFieldPlotLayout instance and adds it to the layout
        self.electric_field_plot = ElectricFieldPlotLayout(tower)
        self.electric_field.add_widget(self.electric_field_plot)

        # create an MagneticFieldPlotLayout instance and adds it to the layout
        self.magnetic_field_plot = MagneticFieldPlotLayout(tower)
        self.magnetic_field.add_widget(self.magnetic_field_plot)

        self.table_layout_x = None

    def update_plots(self):
        """This method prompts the update of all plots and table."""
        self.audible_noise_plot.plot_audible_noise()
        self.electric_field_plot.plot_electric_field()
        self.magnetic_field_plot.plot_magnetic_field()
        self.table_layout.update_table()

    def export_png(self, path, filename, plot):
        """This method prompts the export of a plot to a PNG image according
        to the type of plot chosen in the plot input variable.
        """
        if plot == "Audible Noise":
            self.audible_noise_plot.export_canvas_to_png(path, filename)
        elif plot == "Electric Field":
            self.electric_field_plot.export_canvas_to_png(path, filename)
        elif plot == "Magnetic Field":
            self.magnetic_field_plot.export_canvas_to_png(path, filename)

    def reset_settings_parser(self):
        """This method prompts the settings parser belonging to the plots to
        reload configurations from the buzz.ini file"""
        self.audible_noise_plot.reset_settings_parser()
        self.electric_field_plot.reset_settings_parser()
        self.magnetic_field_plot.reset_settings_parser()

    def export_csv(self, path, filename, loadedJSON=None):
        """This method saves the data of the current plots and table into a CSV
        file.
        """

        # create an instance of SettingsParser to get the calculation settings
        settings_parser = SettingsParser()

        if not filename.endswith(".csv"):
            filename += ".csv"
        with open(os.path.join(path, filename), "w", newline="", encoding="utf-8") as csvfile:
            delimiter = settings_parser.get_csv_delimiter()
            dec_sep = settings_parser.get_csv_decimal()

            writer = csv.writer(csvfile, delimiter=delimiter)
            writer.writerows(
                [
                    ["Calculation Settings"],
                    [],
                ]
                + settings_data_rows(str(loadedJSON), settings_parser)
                + [
                    [],
                    ["Tower Configuration"],
                    [],
                ]
            )

            for system in self.tower.systems:
                writer.writerow(
                    [
                        "System Type:",
                        system.system_type.upper(),
                        "Voltage [kV]:",
                        f"{system.voltage / 1000:.2f}".replace(".", dec_sep),
                        "Current [kA]:",
                        f"{system.current / 1000:.3f}".replace(".", dec_sep),
                    ]
                )
                writer.writerow(
                    [
                        "Line Type",
                        "X-Coordinate [m]",
                        "Y-Coordinate[m]",
                        "No. of Conductors",
                        "Conductor Radius [mm]",
                        "Bundle Radius [mm]",
                        "Conductor Angle Offset [deg]",
                    ]
                )
                for line in system.lines:
                    writer.writerow(
                        [
                            line.line_type,
                            f"{line.line_x:.2f}".replace(".", dec_sep),
                            f"{line.line_y:.2f}".replace(".", dec_sep),
                            line.num_con,
                            f"{line.con_radius * 1000:.2f}".replace(".", dec_sep),
                            f"{line.bundle_radius * 1000:.2f}".replace(".", dec_sep),
                            f"{line.con_angle_offset:.2f}".replace(".", dec_sep),
                        ]
                    )
                writer.writerow([])

            # add audible noise plot data
            writer.writerows(
                [
                    ["Audible Noise"],
                    [],
                    ["Surface Field Gradients and Generated Acoustic Power"],
                    [],
                ]
            )

            # split the table data list of 10 columns into multiple subarrays
            self.table_layout_x = TableLayout(self.tower)

            table_data = self.table_layout_x.headers + self.table_layout_x.get_table_data()
            self.table_layout_x = None

            table_data = [table_data[i : i + 10] for i in range(0, len(table_data), 10)]
            # write table data into csv file
            for data in table_data:
                writer.writerow([str(x).replace(".", dec_sep) for x in data])

            writer.writerows([[], ["Sound Pressure Level [dBA]"], []])
            gp = ["Ground Points"] + [
                str(x).replace(".", dec_sep) for x in self.audible_noise_plot.plot.an_ground_points
            ]
            writer.writerow(gp)
            an_ac_epri = ["AN AC EPRI"] + [
                str(x).replace(".", dec_sep) for x in self.audible_noise_plot.plot.an_ac_epri
            ]

            writer.writerow(an_ac_epri)
            an_ac_bpa = ["AN AC BPA"] + [
                str(x).replace(".", dec_sep) for x in self.audible_noise_plot.plot.an_ac_bpa
            ]
            writer.writerow(an_ac_bpa)
            an_dc_epri = ["AN DC EPRI"] + [
                str(x).replace(".", dec_sep) for x in self.audible_noise_plot.plot.an_dc_epri
            ]
            writer.writerow(an_dc_epri)
            an_dc_bpa = ["AN DC BPA"] + [
                str(x).replace(".", dec_sep) for x in self.audible_noise_plot.plot.an_dc_bpa
            ]
            writer.writerow(an_dc_bpa)
            an_dc_criepi = ["AN DC CRIEPI"] + [
                str(x).replace(".", dec_sep) for x in self.audible_noise_plot.plot.an_dc_criepi
            ]
            writer.writerow(an_dc_criepi)

            # add empty row
            writer.writerow([])

            # add electric field plot data
            writer.writerow(["Electric Field [kV/m]"])
            gp, height = zip(
                *(
                    [("X-Coordinates", "Y-Coordinates")]
                    + [
                        (
                            str(x).replace(".", dec_sep),
                            str(self.electric_field_plot.plot.ef_height_above_ground).replace(
                                ".", dec_sep
                            ),
                        )
                        for x in self.electric_field_plot.plot.ef_ground_points
                    ]
                )
            )
            writer.writerow(gp)
            writer.writerow(height)
            E_ac = ["AC Electric Field"] + [
                str(x).replace(".", dec_sep) for x in self.tower.E_ac_ground
            ]

            writer.writerow(E_ac)
            E_dc = ["DC Electric Field"] + [
                str(x).replace(".", dec_sep) for x in self.tower.E_dc_ground
            ]

            writer.writerow(E_dc)

            # add empty row
            writer.writerow([])

            # add magnetic field plot data
            writer.writerow(["Magnetic Field [uT]"])
            gp, height = zip(
                *(
                    [("X-Coordinates", "Y-Coordinates")]
                    + [
                        (
                            str(x).replace(".", dec_sep),
                            str(self.magnetic_field_plot.plot.mf_height_above_ground).replace(
                                ".", dec_sep
                            ),
                        )
                        for x in self.magnetic_field_plot.plot.mf_ground_points
                    ]
                )
            )
            writer.writerow(gp)
            writer.writerow(height)
            B_ac = ["AC Magnetic Field"] + [str(x).replace(".", dec_sep) for x in self.tower.B_ac]
            writer.writerow(B_ac)
            B_dc = ["DC Magnetic Field"] + [str(x).replace(".", dec_sep) for x in self.tower.B_dc]
            writer.writerow(B_dc)
