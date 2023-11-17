"""Shared functionality for output (csv / pdf)."""

from datetime import datetime


def settings_data_rows(config_path: str, settings_parser) -> list[list[str]]:
    """Assembles info about settings in table format (nested list of strings)."""
    return [
        ["Loaded JSON File:", config_path],
        [
            "Report Generated on:",
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        ],
        [
            "Number of Contour Points (CSM):",
            settings_parser.get_ef_num_contour(),
        ],
        ["Altitude:", settings_parser.get_an_altitude()],
        [
            "Rain Rate (default is 0.8):",
            settings_parser.get_ac_epri_rain_corr(),
        ],
        ["AC EPRI Weather:", settings_parser.get_ac_epri_weather()],
        [
            "AC EPRI DC Offset:",
            str(bool(settings_parser.get_ac_epri_offset())),
        ],
        ["AC BPA Weather:", settings_parser.get_ac_bpa_weather()],
        ["AC BPA DC Offset:", str(bool(settings_parser.get_ac_bpa_offset()))],
        ["DC EPRI Weather:", settings_parser.get_dc_epri_weather()],
        ["DC EPRI Season:", settings_parser.get_dc_epri_season()],
        ["DC BPA Weather:", settings_parser.get_dc_bpa_weather()],
        ["DC BPA Season:", settings_parser.get_dc_bpa_season()],
    ]
