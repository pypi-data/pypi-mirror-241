"""Physical model for a conductor."""

import numpy as np


class Conductor:
    """Conductor is a representation of a conductor in a bundle
    with contour points and simulated charge points.

    initialization variable(s):

    * con_x: x-coordinates of the conductor midpoint
    * con_y: y-coordinates of the conductor midpoint

    The contour points, simulated charge points, mirror charge points and
    unit vectors are collected in an array of dicts. The number of these points
    is defined just before the electric field calculation is done.
    """

    def __init__(self, con_x, con_y):
        # save input variables as object variables
        self.con_x = con_x
        self.con_y = con_y
        self.contours = []
        self.charges = []
        self.mirror_charges = []
        self.unit_vec = []

    def set_con_x(self, con_x):
        """This method sets the x-coordinates of the conductor midpoint."""
        self.con_x = con_x

    def set_con_y(self, con_y):
        """This method sets the y-coordinates of the conductor midpoint."""
        self.con_y = con_y

    def set_points(self, contour_radius, num_contour):
        """This method calculates the contour points, simulated charges
        points, mirror charge points and unit vectors
        """

        # convert the number of contour points into an integer
        num_contour = int(num_contour)

        # calculate the radius of the simulated charge
        charge_radius = contour_radius / (1 + 2 * np.sin(np.pi / num_contour))

        contours = []
        charges = []
        mirror_charges = []
        unit_vec = []

        for i in range(num_contour):
            # calculate the contour points
            contour_x = self.con_x + contour_radius * np.cos(2 * np.pi * i / num_contour)
            contour_y = self.con_y + contour_radius * np.sin(2 * np.pi * i / num_contour)
            contours.append({"x": contour_x, "y": contour_y})

            # calculate the simulated charge points
            # the simulated charge points have a smaller radius compared to the
            # contour points
            charge_x = self.con_x + charge_radius * np.cos(2 * np.pi * i / num_contour)
            charge_y = self.con_y + charge_radius * np.sin(2 * np.pi * i / num_contour)
            charges.append({"x": charge_x, "y": charge_y})

            # calculate the mirror charge points
            # the mirror charge points have the same x-coordinate as the
            # corresponding simulated charge point but a negative y-coordinate
            mirror_charges.append({"x": charge_x, "y": -charge_y})

            # calculate the unit vectors
            arg = 2 * np.pi * i / num_contour
            dir_x = np.cos(arg)
            dir_y = np.sin(arg)
            unit_vec.append({"x": dir_x, "y": dir_y})

        # the arrays of dicts containing the points should be object variables
        self.contours = contours
        self.charges = charges
        self.mirror_charges = mirror_charges
        self.unit_vec = unit_vec
