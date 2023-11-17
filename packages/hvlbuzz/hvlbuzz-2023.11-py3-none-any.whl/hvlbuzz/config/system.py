"""Ui base config for a system. Used in multiple widgets."""

from kivy.properties import ObjectProperty  # pylint: disable=no-name-in-module


class SystemConfigBase:
    """Shared fields between SystemAddPopup and SystemConfig."""

    system_type = ObjectProperty(None)
    voltage = ObjectProperty(None)
    current = ObjectProperty(None)
    con_radius = ObjectProperty(None)
    num_con = ObjectProperty(None)
    bundle_radius = ObjectProperty(None)
    con_angle_offset = ObjectProperty(None)
