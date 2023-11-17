"""Ui Layouts for configuration."""

from kivy.properties import ObjectProperty  # pylint: disable=no-name-in-module
from kivy.uix.boxlayout import BoxLayout

import numpy as np

from .system import SystemConfigBase


class SystemConfig(BoxLayout, SystemConfigBase):
    """SystemConfig is a Layout contained under ConfigLayout which enables user
    to configure parameters which belong to the electrcial system level, namely:

    * voltage
    * current
    * number of conductors
    * conductor radius
    * bundle radius
    * conductor angle offset

    initialization variable(s):

    * system: System class instance to be configured

    The units used for the entry by users are different from those used in
    the calculation backend of the Tower class. The SystemConfig object handles
    the unit conversion from and to the calculation backend.

    Changes to the voltage and current values of a ground line are disabled.

    The layout of the SystemConfig class is defined in the buzz.kv file.
    """

    def __init__(self, system):
        super().__init__()

        # the system to be configured
        self.system = system

        # initialize the contents of the inputs
        self.system_type.text = system.get_system_type()
        self.voltage.text = system.get_voltage()
        self.current.text = system.get_current()
        self.num_con.text = system.get_num_con()
        self.con_radius.text = (
            system.get_con_diameter()
        )  # We want to show the diameter rather than the radius in the GUI
        self.bundle_radius.text = (
            system.get_bundle_spacing()
        )  # We want to show the spacing rather than the radius in the GUI
        self.con_angle_offset.text = system.get_con_angle_offset()

        # disable change to text if system type is ground line
        if self.system.system_type == "gnd":
            self.voltage.disabled = True
            self.current.disabled = True

    def input_check(self):
        """This method checks if all the input values are not empty."""
        empty_counter = 0
        # check voltage value
        if len(self.voltage.text) == 0:
            empty_counter += 1
            self.voltage.background_color = [1, 0, 0, 0.2]
        else:
            self.voltage.background_color = [1, 1, 1, 1]
        # check current value
        if len(self.current.text) == 0:
            empty_counter += 1
            self.current.background_color = [1, 0, 0, 0.2]
        else:
            self.current.background_color = [1, 1, 1, 1]
        # check number of conductors value
        if len(self.num_con.text) == 0:
            empty_counter += 1
            self.num_con.background_color = [1, 0, 0, 0.2]
        else:
            self.num_con.background_color = [1, 1, 1, 1]
        # check conductor radius value
        if len(self.con_radius.text) == 0:
            empty_counter += 1
            self.con_radius.background_color = [1, 0, 0, 0.2]
        else:
            self.con_radius.background_color = [1, 1, 1, 1]
        # check bundle radius value
        if len(self.bundle_radius.text) == 0:
            empty_counter += 1
            self.bundle_radius.background_color = [1, 0, 0, 0.2]
        else:
            self.bundle_radius.background_color = [1, 1, 1, 1]
        # check conductor angle offset value
        if len(self.con_angle_offset.text) == 0:
            empty_counter += 1
            self.con_angle_offset.background_color = [1, 0, 0, 0.2]
        else:
            self.con_angle_offset.background_color = [1, 1, 1, 1]

        return empty_counter == 0

    def set_params(self):
        """This method saves the current values in the input to their
        corresponding variables in the System and Line instances.
        """
        # check that inputs are correct
        if not self.input_check():
            return False

        # convert voltage from kV to V and save it
        voltage = float(self.voltage.text) * 1000
        self.system.set_voltage(voltage)
        # convert current from kA to A and save it
        current = float(self.current.text) * 1000
        self.system.set_current(current)
        # save number of conductors value
        self.system.set_num_con(int(self.num_con.text))
        # convert conductor diameter in mm to radius in m and save it
        con_radius = float(self.con_radius.text) / 2000
        self.system.set_con_radius(con_radius)
        # convert bundle spacing in mm to bundle radius in m and save it
        bundle_spacing = float(self.bundle_radius.text) / 1000
        bundle_radius = bundle_spacing / (2 * np.sin(np.pi / int(self.num_con.text)))
        self.system.set_bundle_radius(bundle_radius)
        # save conductor angle offset value
        self.system.set_con_angle_offset(float(self.con_angle_offset.text))

        return True


class LineConfig(BoxLayout):
    """LineConfig is a Layout contained under ConfigLayout which enables user
    to configure the x- and y-coordinates of a specific line. Since AC and DC
    systems usually contain more than one line, the ConfigLayout instance will
    hold more than one LineConfig instances in an Accordion widget.

    initialization variable(s):

    * line: Line class instance to be configured

    The layout of the LineConfig class is defined in the buzz.kv file.
    """

    title = ObjectProperty(None)
    line_x = ObjectProperty(None)
    line_y = ObjectProperty(None)

    def __init__(self, line):
        super().__init__()

        # the line to be configured
        self.line = line

        # initialize the title
        self.title.text = self.get_line_title(line.line_type)

        # initialize the contents of the inputs
        self.line_x.text = str(line.line_x)
        self.line_y.text = str(line.line_y)

    def input_check(self):
        """This method checks if all the input values are not empty."""
        empty_counter = 0
        # check x-coordinate into line_x variable
        if len(self.line_x.text) == 0 or (self.line_x.text == "-"):
            empty_counter += 1
            self.line_x.background_color = [1, 0, 0, 0.2]
        else:
            self.line_x.background_color = [1, 1, 1, 1]
        # check y-coordinate into line_y variable
        if len(self.line_y.text) == 0 or (self.line_y.text == "-"):
            empty_counter += 1
            self.line_y.background_color = [1, 0, 0, 0.2]
        else:
            self.line_y.background_color = [1, 1, 1, 1]

        if self.line.num_con < 2 and self.line.bundle_radius != 0:
            self.line.bundle_radius = 0
        if self.line.num_con > 1 and self.line.bundle_radius == 0:
            self.line.num_con = 1

        return empty_counter == 0

    def set_params(self):
        """This method saves the current x- and y-coordinate values in the
        input to their corresponding variables in the Line instance.
        """
        # check that the inputs are correct
        if not self.input_check():
            return False

        # save x-coordinate into line_x variable
        self.line.set_line_x(float(self.line_x.text))
        # save y-coordinate into line_y variable
        self.line.set_line_y(float(self.line_y.text))

        return True

    def get_line_title(self, line_type):
        """This method gives the proper AccordionItem title according to the
        line type of the Line instance to be configured.
        The input is the line type string of the Line instance.
        """
        if line_type == "ac_r":
            title = "Line AC R"
        elif line_type == "ac_s":
            title = "Line AC S"
        elif line_type == "ac_t":
            title = "Line AC T"
        elif line_type == "dc_pos":
            title = "Line DC +"
        elif line_type == "dc_neg":
            title = "Line DC -"
        elif line_type == "dc_neut":
            title = "Line DC Neutral"
        elif line_type == "gnd":
            title = "Line GND"
        return title


class ConfigLayout(BoxLayout):
    """ConfigLayout is a Layout contained under the MainLayout instance. It
    contains the SystemConfig and the LineConfig instances which enable users
    to modifiy the parameters of the electrical systems and lines already
    contained in the tower configuration.

    initialization variable(s):

    * tower: Tower class instance to be configured

    The system to be shown in ConfigLayout can be chosen with the dropdown in
    the instance of the SystemSelector class contained in the Toolbar instance.
    """

    system_config_layout = ObjectProperty(None)
    line_configs_layout = ObjectProperty(None)

    def __init__(self, tower, **kwargs):
        super().__init__(**kwargs)

        # change the BoxLayout orientation to vertical
        self.orientation = "vertical"

        # reference to the tower instance to be configured
        self.tower = tower

        # set the config references to none on initialization
        self.system_config = None
        self.line_configs = None
        self.active_system_idx = None
        self.active_system = None

    def set_active_system(self, system_idx):
        """This method is called by the dropdown in the SystemSelector class.
        The input is the integer index of the system to be configured in the
        systems array of the tower instance.
        """

        # set the parameters before changing the active system
        status = self.set_params()

        # only change the active system if set_params was successful
        if status:
            # save the active system index for system removal by ConfigToolbar
            self.active_system_idx = system_idx
            # get the system instance to be shown in the configuration
            self.active_system = self.tower.systems[system_idx]

            # clear any existing widgets from previous active system
            self.system_config_layout.clear_widgets()
            self.line_configs_layout.clear_widgets()

            # add the SystemConfig instance as a child widget
            self.system_config = SystemConfig(self.active_system)
            self.system_config_layout.add_widget(self.system_config)

            # add the LineConfig instances as an Accordion child widget
            self.line_configs = []
            layout = BoxLayout(orientation="vertical")
            for line in self.active_system.lines:
                line_config = LineConfig(line)
                self.line_configs.append(line_config)
                layout.add_widget(line_config)
            self.line_configs_layout.add_widget(layout)

        return status

    def remove_active_system(self):
        """The ConfigLayout should be cleared and the active_system_idx variable
        deleted when the active system is removed by ConfigToolbar."""
        self.system_config_layout.clear_widgets()
        self.line_configs_layout.clear_widgets()
        try:
            del self.active_system_idx
        except AttributeError:
            pass

    def set_params(self):
        """This method prompts the set_params methods in the SystemConfig and
        LineConfig instances.
        """

        # only check system config if it is set
        if self.system_config:
            system_status = self.system_config.set_params()
        else:
            system_status = True

        # only check line configs if the are set
        if self.line_configs:
            line_status = []
            for line_config in self.line_configs:
                line_status.append(line_config.set_params())
        else:
            line_status = [True]

        return system_status and sum(line_status) == len(line_status)
