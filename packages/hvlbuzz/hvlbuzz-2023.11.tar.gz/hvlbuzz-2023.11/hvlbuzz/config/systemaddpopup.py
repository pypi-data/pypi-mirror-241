"""Ui component SystemAddPopup."""

from kivy.properties import ObjectProperty  # pylint: disable=no-name-in-module
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.popup import Popup

import numpy as np

from ..physics.system import System
from ..physics.line import Line
from .system import SystemConfigBase


class SystemAddPopup(Popup, SystemConfigBase):
    """SystemAddPopup enables the users to add an new System instance to the
    tower configuration.

    initialization variable(s):

    * tower: Tower instance on which the new system is to be added
    * system_selector: SystemSelector instance used for system selection
    * data_tabbed_panel: DataTabbedPanel instance containing plots

    The layout of the SystemAddPopup class is defined in the buzz.kv file.
    """

    line_one_x = ObjectProperty(None)
    line_two_x = ObjectProperty(None)
    line_three_x = ObjectProperty(None)
    line_one_y = ObjectProperty(None)
    line_two_y = ObjectProperty(None)
    line_three_y = ObjectProperty(None)
    line_one_label = ObjectProperty(None)
    line_two_label = ObjectProperty(None)
    line_three_label = ObjectProperty(None)

    def __init__(self, tower, system_selector, data_tabbed_panel, **kwargs):
        super().__init__(**kwargs)

        # Tower instance on which the new system is to be added
        self.tower = tower
        # SystemSelector instance used for system selection
        self.system_selector = system_selector
        # DataTabbedPanel instance containing plots
        self.data_tabbed_panel = data_tabbed_panel

        # setup the dropdown for system type selection
        self.setup_dropdown()

        # create a list containing all inputs for input checks
        self.param_input_list = [
            self.system_type,
            self.voltage,
            self.current,
            self.con_radius,
            self.num_con,
            self.bundle_radius,
            self.con_angle_offset,
            self.line_one_x,
            self.line_two_x,
            self.line_three_x,
            self.line_one_y,
            self.line_two_y,
            self.line_three_y,
        ]

    def setup_dropdown(self):
        """sets up the dropdown for system type selection."""

        # create a DropDown instance
        self.dropdown = DropDown()
        # possible system types
        system_types = ["AC", "DC Bipolar", "DC with Neutral Line", "Ground Line"]
        # add buttons to dropdown
        for val in system_types:
            btn = Button(text=val, size_hint_y=None, height=44)
            btn.bind(  # pylint: disable=no-member
                on_release=lambda btn: self.dropdown.select(btn.text)
            )
            self.dropdown.add_widget(btn)
        # bind system_type button click to open dropdown
        self.system_type.bind(on_release=self.dropdown.open)
        # bind dropdown selection to set_system_type method
        self.dropdown.bind(  # pylint: disable=no-member
            on_select=lambda instance, x: self.set_system_type(x)
        )

    def set_ac(self):
        """Set ac system type."""
        self.voltage.text = ""
        self.voltage.disabled = False
        self.current.text = ""
        self.current.disabled = False
        self.line_one_label.text = "AC R"
        self.line_two_label.text = "AC S"
        self.line_two_x.disabled = False
        self.line_two_x.opacity = 1
        self.line_two_y.disabled = False
        self.line_two_y.opacity = 1
        self.line_three_label.text = "AC T"
        self.line_three_x.disabled = False
        self.line_three_x.opacity = 1
        self.line_three_y.disabled = False
        self.line_three_y.opacity = 1

    def set_dc_bipolar(self):
        """Set dc bipolar system type."""
        self.voltage.text = ""
        self.voltage.disabled = False
        self.current.text = ""
        self.current.disabled = False
        self.line_one_label.text = "DC +"
        self.line_two_label.text = "DC -"
        self.line_two_x.disabled = False
        self.line_two_x.opacity = 1
        self.line_two_y.disabled = False
        self.line_two_y.opacity = 1
        self.line_three_label.text = ""
        self.line_three_x.disabled = True
        self.line_three_x.opacity = 0
        self.line_three_y.disabled = True
        self.line_three_y.opacity = 0

    def set_dc_with_neutral_line(self):
        """Set "dc with neutral" system type."""
        self.voltage.text = ""
        self.voltage.disabled = False
        self.current.text = ""
        self.current.disabled = False
        self.line_one_label.text = "DC +"
        self.line_two_label.text = "DC -"
        self.line_two_x.disabled = False
        self.line_two_x.opacity = 1
        self.line_two_y.disabled = False
        self.line_two_y.opacity = 1
        self.line_three_label.text = "DC Neutral"
        self.line_three_x.disabled = False
        self.line_three_x.opacity = 1
        self.line_three_y.disabled = False
        self.line_three_y.opacity = 1

    def set_ground_line(self):
        """Set "ground line" system type."""
        self.voltage.text = "0"
        self.voltage.disabled = True
        self.current.text = "0"
        self.current.disabled = True
        self.line_one_label.text = "Ground Line"
        self.line_two_label.text = ""
        self.line_two_x.disabled = True
        self.line_two_x.opacity = 0
        self.line_two_y.disabled = True
        self.line_two_y.opacity = 0
        self.line_three_label.text = ""
        self.line_three_x.disabled = True
        self.line_three_x.opacity = 0
        self.line_three_y.disabled = True
        self.line_three_y.opacity = 0

    def set_system_type(self, system_type):
        """change the SystemAddPopup layout according to system type chosen."""

        # change the text of the system type button
        self.system_type.text = system_type

        system_type_by_text = {
            "AC": self.set_ac,
            "DC Bipolar": self.set_dc_bipolar,
            "DC with Neutral Line": self.set_dc_with_neutral_line,
            "Ground Line": self.set_ground_line,
        }
        system_type_by_text[system_type]()

    def cancel(self):
        """This method is called when the Cancel button is pressed."""
        self.dismiss()
        self.input_clear()

    def input_check(self):
        """This method checks whether inputs are empty."""
        empty_input_count = 0
        for number_input in self.param_input_list:
            if number_input.text == "" and not number_input.disabled:
                # change background to red if input is empty
                number_input.background_color = [1, 0, 0, 0.2]
                empty_input_count += 1
            else:
                # change background to white if input is not empty
                number_input.background_color = [1, 1, 1, 1]

        return empty_input_count <= 0

    def input_clear(self):
        """This method clears the inputs."""
        for number_input in self.param_input_list:
            number_input.text = ""
            number_input.background_color = [1, 1, 1, 1]

    def suggest_con_angle_offset(self, num_con):
        """This method suggests the appropriate conductor angle offset
        depending on the number of conductors. The conductor angle offset
        will be updated immediately when the number of conductor is changed
        due to the method binding.
        """
        if num_con == "":
            self.con_angle_offset.text = ""
        elif num_con == "3":
            # the typical angle offset for 3 conductors is 30 degrees
            self.con_angle_offset.text = "30"
        elif num_con == "4":
            # the typical angle offset for 4 conductors is 45 degrees
            self.con_angle_offset.text = "45"
        else:
            self.con_angle_offset.text = "0"

    def add_system(self):
        """This method adds a new system to the tower configuration. The units
        used for inputs by users are different from those used in the backend
        calculation. This method handles the unit conversion.
        """

        # check that input is not empty
        input_status = self.input_check()
        if not input_status:
            return

        # prepare the system type string
        system_type_by_text = {
            "AC": "ac",
            "DC with Neutral Line": "dc",
            "DC Bipolar": "dc_bipol",
            "Ground Line": "gnd",
        }
        system_type = system_type_by_text[self.system_type.text]

        # convert voltage from kV to V
        voltage = float(self.voltage.text) * 1000

        # convert current from kA to A
        current = float(self.current.text) * 1000

        num_con = int(self.num_con.text)

        # convert conductor diameter in mm to radius in m
        con_radius = float(self.con_radius.text) / 2000

        # convert bundle spacing in mm to bundle radius in m
        bundle_spacing = float(self.bundle_radius.text) / 1000
        bundle_radius = bundle_spacing / (2 * np.sin(np.pi / num_con))

        if num_con < 2 and bundle_radius != 0:
            bundle_radius = 0
        if num_con > 1 and bundle_radius == 0:
            num_con = 1

        con_angle_offset = float(self.con_angle_offset.text)

        # creates a new System instance with the inputs
        system = System(system_type, voltage, current)

        if not self.line_one_x.disabled and not self.line_one_y.disabled:
            line_type_by_system = {
                "ac": "ac_r",
                "dc": "dc_pos",
                "dc_bipol": "dc_pos",
                "gnd": "gnd",
            }
            line = Line(
                line_type=line_type_by_system[system_type],
                line_x=float(self.line_one_x.text),
                line_y=float(self.line_one_y.text),
                con_radius=con_radius,
                num_con=num_con,
                bundle_radius=bundle_radius,
                con_angle_offset=con_angle_offset,
            )
            system.add_line(line)

        if not self.line_two_x.disabled and not self.line_two_y.disabled:
            line_type_by_system = {"ac": "ac_s", "dc": "dc_neg", "dc_bipol": "dc_neg"}
            line = Line(
                line_type=line_type_by_system[system_type],
                line_x=float(self.line_two_x.text),
                line_y=float(self.line_two_y.text),
                con_radius=con_radius,
                num_con=num_con,
                bundle_radius=bundle_radius,
                con_angle_offset=con_angle_offset,
            )
            system.add_line(line)

        if not self.line_three_x.disabled and not self.line_three_y.disabled:
            line_type_by_system = {"ac": "ac_t", "dc": "dc_neut"}
            line = Line(
                line_type=line_type_by_system[system_type],
                line_x=float(self.line_three_x.text),
                line_y=float(self.line_three_y.text),
                con_radius=con_radius,
                num_con=num_con,
                bundle_radius=bundle_radius,
                con_angle_offset=con_angle_offset,
            )
            system.add_line(line)

        # adds the new System instannce to the tower systems array
        tower_status = self.tower.add_system(system)

        if not tower_status:
            # if tower_status is empty array, the addition was successful
            self.input_clear()
            self.system_selector.setup_system_select()
            self.data_tabbed_panel.update_plots()
            self.dismiss()
        else:
            # if tower_status is a non-empty array, the addition failed

            # tower_status contains the line indexes 0, 1 or 2 which coincide
            # with other lines. Those lines will be marked red.
            if 0 in tower_status:
                self.line_one_x.background_color = [1, 0, 0, 0.2]
                self.line_one_y.background_color = [1, 0, 0, 0.2]
            if 1 in tower_status:
                self.line_two_x.background_color = [1, 0, 0, 0.2]
                self.line_two_y.background_color = [1, 0, 0, 0.2]
            if 2 in tower_status:
                self.line_three_x.background_color = [1, 0, 0, 0.2]
                self.line_three_y.background_color = [1, 0, 0, 0.2]
