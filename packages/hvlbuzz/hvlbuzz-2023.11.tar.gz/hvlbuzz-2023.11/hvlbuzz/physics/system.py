"""Physical model for a system."""

import numpy as np


class System:
    """System contains a collection of lines belonging to the same system.
    A system can have any of the following voltage signal form: AC, DC, GND

    initialization varibale(s):

    * system_type: string containing the current type ('ac', 'dc', 'gnd')
    * voltage: (rms phase-to-phase voltage for AC)

    The lines belonging to the system are collected in an array of objects.
    """

    def __init__(self, system_type, voltage, current):
        # save input variables as object variables
        self.system_type = system_type
        self.voltage = voltage
        self.current = current

        # the lines array contain the line instances belonging to this system
        self.lines = []

    def add_line(self, line):
        """This method adds a Line instance to the lines list."""
        self.lines.append(line)

    def get_system_type(self):
        """This method returns the system type as string in uppercase"""
        return self.system_type.upper()

    def get_voltage(self):
        """This method returns the voltage as string in the unit kV."""
        return str(self.voltage / 1000)

    def set_voltage(self, voltage):
        """This method sets the voltage of the system."""
        self.voltage = voltage

    def get_current(self):
        """This method returns the current as string in the unit kA."""
        return str(self.current / 1000)

    def set_current(self, current):
        """This method sets the current of the system."""
        self.current = current

    def get_num_con(self):
        """This method returns the number of conductor in lines if identical.
        The return value is a string."""
        num_con = [line.num_con for line in self.lines]
        if self.check_equal(num_con):
            return str(num_con[0])
        return ""

    def set_num_con(self, num_con):
        """This method sets the number of conductor in a system bundle."""
        for line in self.lines:
            line.set_num_con(num_con)

    def get_con_radius(self):
        """This method returns the conductor radius in lines if identical.
        The return value is a string with the unit mm.
        """
        con_radius = [line.con_radius for line in self.lines]
        if self.check_equal(con_radius):
            return str(con_radius[0] * 1000)
        return ""

    def get_con_diameter(self):
        """This method returns the conductor radius in lines if identical.
        The return value is a string with the unit mm.
        """
        con_radius = [line.con_radius for line in self.lines]
        if self.check_equal(con_radius):
            return str(con_radius[0] * 2000)
        return ""

    def set_con_radius(self, con_radius):
        """This method sets the conductor radius of the system."""
        for line in self.lines:
            line.set_con_radius(con_radius)

    def get_bundle_radius(self):
        """This method returns the bundle radius in lines if identical.
        The return value is a string with the unit mm.
        """
        bundle_radius = [line.bundle_radius for line in self.lines]
        if self.check_equal(bundle_radius):
            return str(bundle_radius[0] * 1000)
        return ""

    def get_bundle_spacing(self):
        """This method returns the bundle spcing in lines if identical.
        The return value is a string with the unit mm.
        """
        bundle_radius = [line.bundle_radius for line in self.lines]
        num_con = [line.num_con for line in self.lines]
        if self.check_equal(bundle_radius) and self.check_equal(num_con):
            radius = bundle_radius[0] * 1000
            n_poly = num_con[0]
            return f"{2 * radius * np.sin(np.pi / n_poly):.2f}".rstrip("0").rstrip(".")
        return ""

    def set_bundle_radius(self, bundle_radius):
        """This method sets the bundle radius of the system."""
        for line in self.lines:
            line.set_bundle_radius(bundle_radius)

    def get_con_angle_offset(self):
        """This method returns the conductor angle offset in lines if
        identical. The return value is a string in the unit degrees.
        """
        con_angle_offset = [line.con_angle_offset for line in self.lines]
        if self.check_equal(con_angle_offset):
            return str(con_angle_offset[0])
        return ""

    def set_con_angle_offset(self, con_angle_offset):
        """This method sets the conductor angle offset of the system."""
        for line in self.lines:
            line.set_con_angle_offset(con_angle_offset)

    def check_equal(self, lst):
        """This is a utility method that checks if all elements are equal"""
        return not lst or [lst[0]] * len(lst) == lst
