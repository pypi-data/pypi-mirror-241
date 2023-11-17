"""Settings management for global settings."""

import os

from kivy.config import ConfigParser


def buzz_ini_path():
    """Path were to persist dialog settings for the GUI."""
    ini_folder = os.path.join(
        os.getenv("APPDATA") if os.name == "nt" else os.path.expanduser("~/.config"),
        "hvlbuzz",
    )

    os.makedirs(ini_folder, exist_ok=True)
    ini_path = os.path.join(ini_folder, "buzz.ini")
    return ini_path


class SettingsParser(ConfigParser):  # pylint: disable=too-many-public-methods
    """SettingsParser reads the settings values from the buzz.ini file.

    app_data_file = ""

    buzz.ini file will be updated every time the settings values is changed
    in the Settings object of the running Kivy BuzzApp.
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.reset()

    def reset(self):
        """This method reloads the settings from the buzz.ini file."""
        self.read(buzz_ini_path())

    ###################### Tower Geometry Settings ######################

    def get_radius_mult(self):
        """This method gets the tower geometry radius multiplier."""
        return float(self.get("Tower Geometry", "radius_mult"))

    def get_tg_auto_axis(self):
        """This method gets the tower geometry auto axis boolean."""
        return self.getint("Tower Geometry", "auto_axis")

    def get_tg_lower_axis(self):
        """This method gets the tower geometry lower axis limit."""
        return float(self.get("Tower Geometry", "lower_axis"))

    def get_tg_upper_axis(self):
        """This method gets the tower geometry upper axis limit."""
        return float(self.get("Tower Geometry", "upper_axis"))

    def get_con_color(self, line_type):
        """Get the color for the conductor scatter plot for different system
        and line types.
        """
        if line_type in ["ac_r", "ac_s", "ac_t"]:
            color = self.get("Tower Geometry", "ac_con_color")
        elif line_type == "dc_pos":
            color = self.get("Tower Geometry", "dc_pos_con_color")
        elif line_type == "dc_neg":
            color = self.get("Tower Geometry", "dc_neg_con_color")
        elif line_type == "dc_neut":
            color = self.get("Tower Geometry", "dc_neut_con_color")
        elif line_type == "gnd":
            color = self.get("Tower Geometry", "gnd_con_color")
        return color

    ###################### Audible Noise Settings ######################

    def get_an_ground_points(self):
        """Get the start and end of ground coordinate points for the audible
        noise calculation.
        """
        ground_points_start = float(self.get("Audible Noise", "ground_points_start"))
        ground_points_end = float(self.get("Audible Noise", "ground_points_end"))
        ground_points_n = int(self.get("Audible Noise", "ground_points_n"))
        return (ground_points_start, ground_points_end, ground_points_n)

    def get_an_auto_axis(self):
        """This method gets the audible noise auto axis boolean."""
        return self.getint("Audible Noise", "auto_axis")

    def get_an_lower_axis(self):
        """This method gets the audible noise lower axis limit."""
        return float(self.get("Audible Noise", "lower_axis"))

    def get_an_upper_axis(self):
        """This method gets the audible noise upper axis limit."""
        return float(self.get("Audible Noise", "upper_axis"))

    def get_an_unit(self):
        """This method gets the unit for acoustic power calculation."""
        return self.get("Audible Noise", "an_unit")

    def get_an_altitude(self):
        """This method gets the audible noise altitude for correction."""
        return float(self.get("Audible Noise", "altitude"))

    def get_ac_epri_bool(self):
        """This method gets AC EPRI calculation boolean."""
        return self.getint("Audible Noise", "ac_epri_bool")

    def get_ac_epri_weather(self):
        """This method gets the AC EPRI weather condition."""
        return self.get("Audible Noise", "ac_epri_weather")

    def get_ac_epri_offset(self):
        """This method gets the AC EPRI offset boolean."""
        return self.getint("Audible Noise", "ac_epri_offset")

    def get_ac_epri_rain_corr(self):
        """This method gets the AC EPRI rain correction factor."""
        try:
            s = self.get("Audible Noise", "ac_epri_rain_corr")
            s = s.replace(",", ".")
            s = "".join(s.split())
            return float(s)
        except ValueError:
            return 0

    def get_ac_bpa_bool(self):
        """This method gets the AC BPA calculation boolean."""
        return self.getint("Audible Noise", "ac_bpa_bool")

    def get_ac_bpa_weather(self):
        """This method gets the AC BPA weather condition."""
        return self.get("Audible Noise", "ac_bpa_weather")

    def get_ac_bpa_offset(self):
        """This method gets the AC EPRI offset boolean."""
        return self.getint("Audible Noise", "ac_bpa_offset")

    def get_dc_epri_bool(self):
        """This method gets the DC EPRI calculation boolean."""
        return self.getint("Audible Noise", "dc_epri_bool")

    def get_dc_epri_weather(self):
        """This method gets the DC EPRI weather condition."""
        return self.get("Audible Noise", "dc_epri_weather")

    def get_dc_epri_season(self):
        """This method gets the DC EPRI seasonal condition."""
        return self.get("Audible Noise", "dc_epri_season")

    def get_dc_bpa_bool(self):
        """This method gets the DC BPA calculation boolean."""
        return self.getint("Audible Noise", "dc_bpa_bool")

    def get_dc_bpa_weather(self):
        """This method gets the DC BPA weather condition."""
        return self.get("Audible Noise", "dc_bpa_weather")

    def get_dc_bpa_season(self):
        """This method gets the DC BPA seasonal condition."""
        return self.get("Audible Noise", "dc_bpa_season")

    def get_dc_criepi_bool(self):
        """This method gets the DC CRIEPI calculation boolean."""
        return self.getint("Audible Noise", "dc_criepi_bool")

    ###################### Electric Field Settings ######################

    def get_ef_num_contour(self):
        """This method gets the number of contour points for the electric field
        calculation.
        """
        return self.getint("Electric Field", "electric_field_num_contour")

    def get_ef_height_above_ground(self):
        """This method gets the height above ground of ground points."""
        return float(self.get("Electric Field", "height_above_ground"))

    def get_ef_ground_points(self):
        """This method gets the start and end of ground coordinate points for
        the electric field calculation on the ground.
        """
        ground_points_start = float(self.get("Electric Field", "ground_points_start"))
        ground_points_end = float(self.get("Electric Field", "ground_points_end"))
        ground_points_n = int(self.get("Electric Field", "ground_points_n"))
        return (ground_points_start, ground_points_end, ground_points_n)

    def get_ef_auto_axis(self):
        """This method gets the electric field auto axis boolean."""
        return self.getint("Electric Field", "auto_axis")

    def get_ef_lower_axis(self):
        """This method gets the electric field axis lower limit."""
        return float(self.get("Electric Field", "lower_axis"))

    def get_ef_upper_axis(self):
        """This method gets the electric field axis upper limit."""
        return float(self.get("Electric Field", "upper_axis"))

    ###################### Magnetic Field Settings ######################

    def get_mf_height_above_ground(self):
        """This method gets the height above ground of ground points."""
        return float(self.get("Magnetic Field", "height_above_ground"))

    def get_mf_ground_points(self):
        """This method gets the start and end of ground coordinate points for
        the magnetic field calculation on the ground.
        """
        ground_points_start = float(self.get("Magnetic Field", "ground_points_start"))
        ground_points_end = float(self.get("Magnetic Field", "ground_points_end"))
        ground_points_n = int(self.get("Magnetic Field", "ground_points_n"))
        return (ground_points_start, ground_points_end, ground_points_n)

    def get_mf_auto_axis(self):
        """This method gets the magnetic field auto axis boolean."""
        return self.getint("Magnetic Field", "auto_axis")

    def get_mf_lower_axis(self):
        """This method gets the magnetic field axis lower limit."""
        return float(self.get("Magnetic Field", "lower_axis"))

    def get_mf_upper_axis(self):
        """This method gets the magnetic field axis upper limit."""
        return float(self.get("Magnetic Field", "upper_axis"))

    ###################### Export Settings ######################

    def get_csv_delimiter(self):
        """This method gets the delimiter for CSV export."""
        return self.get("Export", "csv_delimiter")

    def get_csv_decimal(self):
        """This method gets the decimal separator for CSV export."""
        return self.get("Export", "csv_decimal")

    def get_load_path(self):
        """This method sets the default load path."""
        return self.get("Export", "load_path")

    def get_save_path(self):
        """This method sets the default save path."""
        return self.get("Export", "save_path")

    def get_ecsv_path(self):
        """This method sets the default export csv path."""
        return self.get("Export", "ecsv_path")

    def get_epdf_path(self):
        """This method sets the default export pdf path."""
        return self.get("Export", "epdf_path")

    def get_epng_path(self):
        """This method sets the default export png path."""
        return self.get("Export", "epng_path")
