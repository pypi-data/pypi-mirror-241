"""Ui layout for the system selector."""

import re

# Import Kivy modules
from kivy.properties import ObjectProperty  # pylint: disable=no-name-in-module
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown


class SystemSelector(BoxLayout):
    """SystemSelector is a dropdown that enables the selection of the system
    to be shown on the ConfigLayout instance.

    initialization variable(s):

    * tower: Tower instance to be configured
    * config_layout: ConfigLayout instance where the configuration is shown

    The SystemSelector layout is contained in the buzz.kv file.
    """

    system_selector = ObjectProperty(None)

    def __init__(self, tower, config_layout, **kwargs):
        super().__init__(**kwargs)

        # Tower instance to be configured
        self.tower = tower
        # ConfigLayout instance where the configuration is shown
        self.config_layout = config_layout

        self.dropdown = DropDown()
        self.active_system = None

    def setup_system_select(self):
        """This method sets up the dropdown with the appropriate buttons."""
        self.dropdown.clear_widgets()
        for system_idx, system in enumerate(self.tower.systems):
            # prepare the button text
            if system.system_type == "ac":
                system_type = "AC"
            elif system.system_type in {"dc", "dc_bipol"}:
                system_type = "DC"
            elif system.system_type == "gnd":
                system_type = "GND"
            title = "System " + str(system_idx + 1) + ": " + system_type
            # create the button
            btn = Button(text=title, size_hint_y=None, height=44)
            btn.bind(  # pylint: disable=no-member
                on_release=lambda btn: self.dropdown.select(btn.text)
            )
            # adds button as a child to the dropdown
            self.dropdown.add_widget(btn)
        self.system_selector.bind(on_release=self.dropdown.open)
        self.dropdown.bind(  # pylint: disable=no-member
            on_select=lambda inst, x: self.set_active_system(x)
        )
        self.system_selector.text = "Select System \u25BC"

    def set_active_system(self, btn_str):
        """This method sets the current active system for configuration."""
        # get the index integer from the button text string
        system_idx = int(re.search("([0-9]+)", btn_str).group(0)) - 1
        # set new active system in the ConfigLayout instance
        status = self.config_layout.set_active_system(system_idx)
        # only change button text if set_active_system was successful
        if status:
            # update the system_selector button text
            self.system_selector.text = btn_str + " \u25BC"
