"""Physical model for a line."""

import numpy as np

from .conductor import Conductor


class Line:
    """Line is a representation of a high voltage line containing conductors.

    initialization varibale(s):

    * line_type:

        * AC: ac_r, ac_s or ac_t depending on phase
        * DC: dc_pos, dc_neg or dc_neut depending on voltage
        * GND: gnd for all ground lines

    * line_x: x-coordinates of the line centre point
    * line_y: y-coordinates of the line centre point
    * con_radius: radius of the individual conductors
    * num_con: number of sub-conductors in bundle
    * bundle_radius: bundle radius
    * con_angle_offset: start angle of the conductor placement. The angle is
        given in degrees with the zero coinciding with the horizontal axis on
        the right-hand-side.

    The conductors belonging to the line are collected in an array of objects.
    """

    def __init__(
        self,
        line_type,
        line_x,
        line_y,
        con_radius,
        num_con,
        bundle_radius,
        con_angle_offset,
    ):
        # save input variables as object variables
        self.line_type = line_type
        self.line_x = line_x
        self.line_y = line_y
        self.con_radius = con_radius
        self.num_con = num_con
        self.bundle_radius = bundle_radius
        self.con_angle_offset = con_angle_offset

        # set the conductor arrays
        self.set_cons()

    def set_line_x(self, line_x):
        """This method sets the x-coordinates of the line midpoint."""
        self.line_x = line_x
        # update conductors concurrently
        self.set_cons()

    def set_line_y(self, line_y):
        """This method sets the y-coordinates of the line midpoint."""
        self.line_y = line_y
        # update conductors concurrently
        self.set_cons()

    def set_con_radius(self, con_radius):
        """This method sets the conductor radius."""
        self.con_radius = con_radius
        # update conductors concurrently
        self.set_cons()

    def set_num_con(self, num_con):
        """This method sets the number of conductors."""
        self.num_con = num_con
        # update conductors concurrently
        self.set_cons()

    def set_bundle_radius(self, bundle_radius):
        """This method sets the bundle radius."""
        self.bundle_radius = bundle_radius
        # update conductors concurrently
        self.set_cons()

    def set_con_angle_offset(self, con_angle_offset):
        """This method sets the conductor angle offset."""
        self.con_angle_offset = con_angle_offset
        # update conductors concurrently
        self.set_cons()

    def set_cons(self):
        """This method creates the Conductor instance of the line."""
        cons = []
        for i in range(self.num_con):
            con_x = self.line_x + self.bundle_radius * np.cos(
                2 * np.pi * i / self.num_con + self.con_angle_offset * np.pi / 180
            )
            con_y = self.line_y + self.bundle_radius * np.sin(
                2 * np.pi * i / self.num_con + self.con_angle_offset * np.pi / 180
            )
            cons.append(Conductor(con_x, con_y))
        self.cons = cons
