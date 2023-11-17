"""Physical model for a tower."""

# pylint: disable=too-many-lines
import json
from enum import Enum

import numpy as np

from .system import System
from .line import Line


class Season(Enum):
    """
    Seasons for audible noise correction
    """

    Summer = "summer"
    Winter = "winter"
    Fall = "fall"
    Spring = "spring"


class AudibleNoiseCorrections:
    """
    Collect all correction term for audible noise calculations
    """

    @staticmethod
    def season_dc_offset_bpa(season: Season) -> int:
        """
        Store the correction terms for the seasons according to BPA calculations.
        Reference: Formulas for Predicting Audible Noise from Overhead High Voltage AC and DC Lines
        by V. L. Chartier and R. D. Stearns
        published 1981 in IEEE Transactions on Power Apparatus and Systems
        page 128 / section "General DC Equation"
        """

        season_dict = {
            Season.Winter: -2,
            Season.Fall: 0,
            Season.Summer: 2,
            Season.Spring: 0,
        }
        return season_dict[season]


class Tower:
    """The Tower class contains the geometrical information of the high voltage
    line systems in a list. Based on this information, the class methods can
    perform the following calculations:

    * Electric field on ground level
    * Magnetic field on ground level
    * Surface gradient on the conductors
    * Audible noise with these empirical formulas:
        * AC EPRI
        * AC BPA
        * DC EPRI
        * DC BPA
        * DC CRIEPI

    The Charge Simulation Method (CSM) is used for the electric field
    calculations. Thus, before the calculation of the electric field and surface
    gradient is performed, the electric field calculation accuracy must be set
    so that the Conductor instances can calculate the number of contour
    points needed for the calculation.
    """

    # epsilon_0 is the vacuum permittivity constant
    epsilon_0 = np.expm1(8.854e-12)
    # mu is the permeability constant in air
    mu_0 = np.expm1(1.2566370614e-6)

    def __init__(self):
        self.systems = []
        self.num_contour = 0
        self.B_ac = np.array([])
        self.B_dc = np.array([])
        self.B_sum = np.array([])
        self.E_ac_ground = np.array([])
        self.E_dc_ground = np.array([])
        self.E_sum_ground = np.array([])
        self.E_ac = np.array([])
        self.E_dc = np.array([])

    def set_num_contour(self, num_contour):
        """This method defines the number of contour points for the charge
        simulation method. The input is an integer with a minimum value of 2.
        """
        self.num_contour = num_contour

    def get_num_contour(self):
        """This method returns the number of contour points defined for the
        charge simulation method calculation of this tower."""
        return self.num_contour

    def add_system(self, system):
        """This method checks for line collision between lines in the existing
        systems and the new system to be added. If there are no line collision,
        the new system is added to the systems list.
        """

        line_idx = []
        for old_system in self.systems:
            for old_line in old_system.lines:
                old_coord = [old_line.line_x, old_line.line_y]
                old_bundle_radius = old_line.bundle_radius
                for new_line_idx, new_line in enumerate(system.lines):
                    new_coord = [new_line.line_x, new_line.line_y]
                    new_bundle_radius = new_line.bundle_radius

                    # calculate the difference between distance between lines
                    # and the sum of the  bundle radius of both lines
                    dist = np.linalg.norm(np.subtract(new_coord, old_coord))
                    sum_bundle_radius = new_bundle_radius + old_bundle_radius
                    diff = dist - sum_bundle_radius

                    # if the difference is less than zero, there is line
                    # collision. save the line index of the colliding new line.
                    if diff < 0:
                        line_idx.append(new_line_idx)

        # add the new system if there is no collision (line_idx is empty)
        if not line_idx:
            self.systems.append(system)

        return line_idx

    def remove_system(self, system_index):
        """This method removes the system on the system_index place in the
        systems list.
        """
        del self.systems[system_index]

    def reset_systems(self):
        """This method empties the systems list."""
        self.systems = []

    def calc_magnetic_field(self, ground_points, height_above_ground):
        """This method calculates the magnetic field on the ground  level
        below the high voltage line conductors. The Biot-Savart formula is
        implemented here for the calculation of magnetic field.

        input variable(s):

        * ground_points: Numpy array containing x-coordinates of ground points
        * height_above_ground: height of ground points

        The calculation will be saved as class variable:

        * B_ac: magnetic field caused by AC conductors [1e-6 T]
        * B_dc: magnetic field caused by DC conductors [1e-6 T]

        The return value is a boolean status signaling the success of the
        calculation:

        * False: calculation aborted
        * True: calculation successful
        """

        # check for line collision
        if self._check_line_collision():
            return False

        # ground points coordinates
        ground_coords = np.column_stack(
            (ground_points, np.full(ground_points.shape, height_above_ground))
        )

        # get conductor coordinates
        cons = []
        for system in self.systems:
            for line in system.lines:
                for con in line.cons:
                    cons.append([con.con_x, con.con_y])

        # calculate the x- and y- component of the v matrix
        cons = np.split(np.array(cons), len(cons))
        diff = np.subtract(ground_coords, cons)
        diff_split = np.dsplit(diff, 2)
        diff_x = diff_split[0].reshape(len(cons), len(ground_coords))
        diff_y = diff_split[1].reshape(len(cons), len(ground_coords))
        dist = np.linalg.norm(diff, axis=2)
        divider = np.multiply(np.square(dist), 2 * np.pi)
        v_x = np.divide(-diff_y, divider)
        v_y = np.divide(diff_x, divider)

        # get the conductor currents
        I = self.calc_currents()

        # calculate the AC magnetic field
        H_ac_x = np.matmul(I["ac"], v_x)
        H_ac_y = np.matmul(I["ac"], v_y)
        H_ac = np.sqrt(np.add(np.square(np.abs(H_ac_x)), np.square(np.abs(H_ac_y))))
        # save the magnetic field in the correct unit [1e-6 T]
        self.B_ac = self.mu_0 * H_ac * 1000000

        # calculate the DC magnetic field
        H_dc_x = np.matmul(I["dc"], v_x)
        H_dc_y = np.matmul(I["dc"], v_y)
        H_dc = np.sqrt(np.add(np.square(np.abs(H_dc_x)), np.square(np.abs(H_dc_y))))
        # save the magnetic field in the correct unit [1e-6 T]
        self.B_dc = self.mu_0 * H_dc * 1000000

        # save the sum of the magnetic fields
        self.B_sum = np.sqrt(np.add(np.square(self.B_ac), np.square(self.B_dc)))

        # return True if calculation is successful
        return True

    def calc_currents(self):
        """This method calculates the corresponding AC and DC conductor currents
        for the magnetic field calculation in calc_magnetic_field.
        """

        I_ac = []
        I_dc = []
        for system in self.systems:
            for line in system.lines:
                for _con in line.cons:
                    # handle AC currents using phasors
                    if system.system_type == "ac":
                        if line.line_type == "ac_r":
                            theta = 0
                        elif line.line_type == "ac_s":
                            theta = -2 * np.pi / 3
                        elif line.line_type == "ac_t":
                            theta = -4 * np.pi / 3
                        I_ac.append(system.current * np.exp(1j * theta))
                        I_dc.append(0)

                    # handle DC currents
                    elif system.system_type in ["dc", "dc_bipol"]:
                        if line.line_type == "dc_pos":
                            I_dc.append(system.current)
                        elif line.line_type == "dc_neg":
                            I_dc.append(-system.current)
                        elif line.line_type == "dc_neut":
                            I_dc.append(0)
                        I_ac.append(0)

                    # set currents of ground lines to zero
                    elif system.system_type == "gnd":
                        I_ac.append(0)
                        I_dc.append(0)

        # return the current lists in a dict
        return {"ac": I_ac, "dc": I_dc}

    def calc_electric_field(self, ground_points, height_above_ground):
        """This method calculates the electric field on the ground level
        below the high voltage line conductors. The Charge Simulation Method
        (CSM) is used for the calculation of electric field.

        input variable(s):

        * ground_points: Numpy array containing x-coordinates of ground points
        * height_above_ground: height of ground points

        The calculation will be saved as class variable:

        * E_ac_ground: electric field caused by AC conductors [kV/cm]
        * E_dc_ground: electric field caused by DC conductors [kV/cm]

        The return value is a boolean status signaling the success of the
        calculation:

        * False: calculation aborted
        * True: calculation successful
        """

        # check for line collision
        if self._check_line_collision():
            return False

        # calculate the constant coefficient for electric field calculation
        coeff = (2 * np.pi * self.epsilon_0) ** -1

        # get the coordinates of contours, charges and mirror charges
        points = self.get_coordinates()
        dim = points["dim"]
        contours = points["contours"]
        charges = points["charges"]
        mirror_charges = points["mirror_charges"]

        # create the array of ground points coordinates
        ground_coords = np.column_stack(
            (ground_points, np.full(ground_points.shape, height_above_ground))
        )

        # calculate the dimension of the ground points and charges arrays
        dim_ground_points = len(ground_points)
        dim_charges = len(charges)

        # split the ground points into singular coordinates
        ground_coords = np.split(np.array(ground_coords), dim_ground_points)

        # calculate the difference between contour points and each of
        # simulated charges points and mirror charge points
        charges_diff = np.subtract(ground_coords, charges)
        mirror_charges_diff = np.subtract(ground_coords, mirror_charges)

        # split the difference into x- and y-coordinates
        charges_diff_split = np.dsplit(charges_diff, 2)
        charges_diff_x = charges_diff_split[0].reshape((dim_ground_points, dim_charges))
        charges_diff_y = charges_diff_split[1].reshape((dim_ground_points, dim_charges))

        mirror_charges_diff_split = np.dsplit(mirror_charges_diff, 2)
        mirror_charges_diff_x = mirror_charges_diff_split[0].reshape(
            (dim_ground_points, dim_charges)
        )
        mirror_charges_diff_y = mirror_charges_diff_split[1].reshape(
            (dim_ground_points, dim_charges)
        )

        # calculate the euclidean distances
        charges_norm = np.linalg.norm(charges_diff, axis=2)
        mirror_charges_norm = np.linalg.norm(mirror_charges_diff, axis=2)

        # calculate the squares of the euclidean distances
        charges_norm_square = np.square(charges_norm)
        mirror_charges_norm_square = np.square(mirror_charges_norm)

        # calculate the x- and y-components of the v matrix
        gp_v_x = np.subtract(
            np.divide(charges_diff_x, charges_norm_square),
            np.divide(mirror_charges_diff_x, mirror_charges_norm_square),
        )
        gp_v_y = np.subtract(
            np.divide(charges_diff_y, charges_norm_square),
            np.divide(mirror_charges_diff_y, mirror_charges_norm_square),
        )

        # calculate the matrices
        matrices = self.calc_matrices(contours, charges, mirror_charges, dim)
        pot_matrix = matrices["pot_matrix"]

        # calculate voltages
        U = self.calc_voltages()

        # calculate the AC electric field on ground
        line_charges_ac = np.linalg.solve(pot_matrix, U["ac"])
        E_ac_x_ground = np.abs(np.matmul(gp_v_x, line_charges_ac))
        E_ac_y_ground = np.abs(np.matmul(gp_v_y, line_charges_ac))
        # save the electric field in the correct unit [kV/m]
        self.E_ac_ground = (
            coeff * np.abs(np.sqrt(np.square(E_ac_x_ground) + np.square(E_ac_y_ground))) / 1000
        )

        # calculate the DC electric field on ground
        line_charges_dc = np.linalg.solve(pot_matrix, U["dc"])
        E_dc_x_ground = np.matmul(gp_v_x, line_charges_dc)
        E_dc_y_ground = np.matmul(gp_v_y, line_charges_dc)
        # save the electric field in the correct unit [kV/m]
        self.E_dc_ground = (
            coeff * np.sqrt(np.square(E_dc_x_ground) + np.square(E_dc_y_ground)) / 1000
        )

        # calculate sum of electric fields
        self.E_sum_ground = np.sqrt(
            np.add(np.square(self.E_ac_ground), np.square(self.E_dc_ground))
        )

        # return True if the calculation is successful
        return True

    def calc_conductor_surface_gradient(self):
        """This method calculates the surface gradients for all conductors on
        the tower.The Charge Simulation Method (CSM) is used for the calculation
        of electric field.

        The calculation will be saved as class variable:

        * E_ac: surface gradient caused by charges in AC conductors [kV/cm]
        * E_dc: surface gradient caused by charges in DC conductors [kV/cm]

        The return value is a boolean status signaling the success of the
        calculation:

        * False: calculation aborted
        * True: calculation successful
        """

        # check for line collision
        if self._check_line_collision():
            return False

        # calculate the constant coefficient for electric field calculation
        coeff = (2 * np.pi * self.epsilon_0) ** -1

        # get the coordinates of contours, charges and mirror charges
        points = self.get_coordinates()
        dim = points["dim"]
        contours = points["contours"]
        charges = points["charges"]
        mirror_charges = points["mirror_charges"]
        unit_vec = points["unit_vec"]

        # split unit vectors into x- and y-components
        unit_vec_split = np.hsplit(np.array(unit_vec), 2)
        unit_vec_x = unit_vec_split[0].reshape(dim)
        unit_vec_y = unit_vec_split[1].reshape(dim)

        # calculate voltages
        U = self.calc_voltages()

        # calculate the matrices
        matrices = self.calc_matrices(contours, charges, mirror_charges, dim)
        pot_matrix = matrices["pot_matrix"]
        v_x = matrices["v_x"]
        v_y = matrices["v_y"]

        # calculate the AC line charges
        line_charges_ac = np.linalg.solve(pot_matrix, U["ac"])
        # calculate the x and y components of the DC electric field
        E_ac_x = np.matmul(v_x, np.abs(line_charges_ac))
        E_ac_y = np.matmul(v_y, np.abs(line_charges_ac))
        # multiply the x and y components with the corresponding unit vectors
        # and summing both terms
        self.E_ac = coeff * (np.multiply(E_ac_x, unit_vec_x) + np.multiply(E_ac_y, unit_vec_y))

        # calculate the DC line charges
        line_charges_dc = np.linalg.solve(pot_matrix, U["dc"])
        # calculate the x and y components of the DC electric field
        E_dc_x = np.matmul(v_x, line_charges_dc)
        E_dc_y = np.matmul(v_y, line_charges_dc)
        # multiply the x and y components with the corresponding unit vectors
        # and summing both terms
        self.E_dc = coeff * (np.multiply(E_dc_x, unit_vec_x) + np.multiply(E_dc_y, unit_vec_y))

        # return True of the calculation is successful
        return True

    def get_coordinates(self):
        """This method gets the contour and charges points as well as the
        unit vectors from all conductors on the tower. These coordinates
        are required for the electric field calculations. The number of
        contour points in each conductor is determined by the calculation
        accuracy (calc_acc).
        """
        contours = []
        charges = []
        mirror_charges = []
        unit_vec = []
        for system in self.systems:
            for line in system.lines:
                for con in line.cons:
                    # prompt the conductors to calculate the contour
                    # points accoding to  the calc_acc value of the tower.
                    con.set_points(line.con_radius, self.get_num_contour())
                    for val in con.contours:
                        contours.append([val["x"], val["y"]])
                    for val in con.charges:
                        charges.append([val["x"], val["y"]])
                    for val in con.mirror_charges:
                        mirror_charges.append([val["x"], val["y"]])
                    for val in con.unit_vec:
                        unit_vec.append([val["x"], val["y"]])

        # return the lists of coordinates in a dict
        return {
            "contours": contours,
            "charges": charges,
            "mirror_charges": mirror_charges,
            "unit_vec": unit_vec,
            # return the dimension, which is same for all matrices
            "dim": len(contours),
        }

    def calc_voltages(self) -> dict[str, list[float]]:
        """This method calculates the conductor voltages which are required for
        the electric field calculations.
        """

        theta = {"ac_r": 0.0, "ac_s": -2 * np.pi / 3, "ac_t": -4 * np.pi / 3}
        v_sign = {"dc_pos": 1.0, "dc_neut": 0.0, "dc_neg": -1.0}

        U_ac = []
        U_dc = []
        for system in self.systems:
            for line in system.lines:
                for con in line.cons:
                    for _contour in con.contours:
                        # handle the AC conductor voltages
                        if system.system_type == "ac":
                            voltage = (
                                system.voltage / np.sqrt(3) * np.exp(1j * theta[line.line_type])
                            )
                            U_ac.append(voltage)
                            U_dc.append(0.0)

                        # handle the DC conductor voltages
                        elif system.system_type in ["dc", "dc_bipol"]:
                            voltage = v_sign[line.line_type] * system.voltage
                            U_ac.append(0.0)
                            U_dc.append(voltage)

                        # set the voltages of ground lines to zero
                        elif system.system_type == "gnd":
                            U_ac.append(0.0)
                            U_dc.append(0.0)

        # return the voltage lists in a dict
        return {"ac": U_ac, "dc": U_dc}

    def calc_matrices(self, contours, charges, mirror_charges, dim):
        """This method calculates the potential and v matrices required for the
        electric field calculation.

        input variable(s):

        * contours: coordinates of contour points in a list
        * charges: coordinates of charges points in a list
        * mirror_charges: coordinates of mirror_charges points in a list
        * dim: length of all lists
        """

        # calculate the coefficient
        coeff = (2 * np.pi * self.epsilon_0) ** -1

        # split the contours into singular coordinates
        contours_split = np.split(np.array(contours), dim)

        # calculate the difference between contour points and each of
        # simulated charges points and mirror charge points
        charges_diff = np.subtract(contours_split, charges)
        mirror_charges_diff = np.subtract(contours_split, mirror_charges)

        # split the difference into x- and y-coordinates
        charges_diff_split = np.dsplit(charges_diff, 2)
        charges_diff_x = charges_diff_split[0].reshape((dim, dim))
        charges_diff_y = charges_diff_split[1].reshape((dim, dim))

        mirror_charges_diff_split = np.dsplit(mirror_charges_diff, 2)
        mirror_charges_diff_x = mirror_charges_diff_split[0].reshape((dim, dim))
        mirror_charges_diff_y = mirror_charges_diff_split[1].reshape((dim, dim))

        # calculate the euclidean distances
        charges_norm = np.linalg.norm(charges_diff, axis=2)
        mirror_charges_norm = np.linalg.norm(mirror_charges_diff, axis=2)

        # calculate the squares of the euclidean distances
        charges_norm_square = np.square(charges_norm)
        mirror_charges_norm_square = np.square(mirror_charges_norm)

        # calculate the potential matrix
        pot_matrix = coeff * np.log(np.divide(mirror_charges_norm, charges_norm))

        # calculate the x- and y-components of the v matrix
        v_x = np.subtract(
            np.divide(charges_diff_x, charges_norm_square),
            np.divide(mirror_charges_diff_x, mirror_charges_norm_square),
        )
        v_y = np.subtract(
            np.divide(charges_diff_y, charges_norm_square),
            np.divide(mirror_charges_diff_y, mirror_charges_norm_square),
        )

        return {"pot_matrix": pot_matrix, "v_x": v_x, "v_y": v_y}

    def calc_ave_max_conductor_surface_gradient(self):
        """This method calculates the average maximum surface gradient of the
        line bundles which is required for the audible noise calculation. This
        method will implicitly call the calc_conductor_surface_gradient and,
        thus, the user interface will only need to call this method if the
        average maximum surface gradient is to be recalculated before the
        audible noise calculations.

        The calculation will be saved as variables of the Line instances:

        * E_ac: average maximum surface gradient of the AC line [kV/cm]
        * E_dc: average maximum surface gradient of the DC line [kV/cm]

        The return value is a boolean status signaling the success of the
        calculation:

        * False: calculation aborted
        * True: calculation successful
        """

        # calculate the complete conductor surface gradient
        status = self.calc_conductor_surface_gradient()
        # abort calculation and return False if conducotr surface gradient
        # calculation cannot be performed
        if not status:
            return False

        try:
            # get the required surface gradient for the corresponding lines
            for sys_idx, system in enumerate(self.systems):
                for line_idx, line in enumerate(system.lines):
                    E_ac_max = []
                    E_dc_max = []
                    for con_idx, con in enumerate(line.cons):
                        # get the start and end indexes of the current line
                        if sys_idx == 0 and line_idx == 0 and con_idx == 0:
                            start = 0
                            end = len(con.contours)
                        else:
                            start = end + 1
                            end += len(con.contours)

                        # get the maximum surface gradients of conductors
                        # in a bundle (minimum for DC negative conductors)
                        E_ac_max.append(np.max(self.E_ac[start:end]))

                        max_val = np.max(self.E_dc[start:end])
                        min_val = np.min(self.E_dc[start:end])
                        if line.line_type == "dc_pos":
                            E_dc_max.append(max_val)
                        elif line.line_type == "dc_neg":
                            E_dc_max.append(min_val)
                        else:
                            E_dc_max.append(np.maximum(max_val, min_val))

                    # save the surface gradient in the correct unit [kV/cm]
                    line.E_ac = np.mean(E_ac_max) / 100000
                    line.E_dc = np.mean(E_dc_max) / 100000

                    # save the offset surface gradient (update: polarity independent)
                    line.E_ac_pos_offset = line.E_ac + np.abs(line.E_dc) / np.sqrt(2)
                    line.E_ac_neg_offset = line.E_ac_pos_offset

                    # include AC ripple (as rms) in DC surface gradient
                    line.E_dc_rip = np.abs(line.E_dc) + line.E_ac

        except AttributeError as e:
            print(e)

        # return True if calculation is successful
        return True

    def _check_line_collision(self):
        """This method checks for colission between lines in the tower geometry
        configuration. If there is at least one line colission, the electric and
        magnetic field calculations cannot be done as this leads to an error
        in the Numpy matrix operation.

        The return value is a list containing tuples of colliding lines.
        """

        line_idx = []
        coords = []
        bundle_radii = []
        for system in self.systems:
            for line in system.lines:
                coords.append([line.line_x, line.line_y])
                bundle_radii.append(line.bundle_radius)

        for i, coords_i in enumerate(coords):
            for j, coords_j in enumerate(coords):
                if i == j:
                    continue
                # calculate the difference between the distance between
                # lines and the sum of bundle radii
                dist = np.linalg.norm(np.subtract(coords_i, coords_j))
                sum_bundle_radii = bundle_radii[i] + bundle_radii[j]
                diff = dist - sum_bundle_radii
                # line colission exists if the difference is negative
                if diff < 0:
                    line_idx.append((i, j))

        return line_idx

    def calc_AN_AC_EPRI(  # pylint: disable=too-many-branches,too-many-statements
        self, ground_points, weather, offset, an_unit, altitude, rain_corr
    ):
        """This method calculates the audible noise of AC lines according to the
        empirical formula defined by EPRI.

        input variable(s):

        * ground_points: Numpy array containing x-coordinates of ground points
        * weather:
            * Foul: default weather condition for the AC EPRI calculation
            * Fair: reduces the audible noise by 25dB
        * offset: boolean value which returns offset audible noise value if true
        * an_unit: offset for the acoustic power calculation depending on unit chosen
        * altitude: audible noise altitude correction in meter
        * rain_corr: the rain rate for the inclusion of rain factor correction in calculation

        The return value is a Numpy array containing the sound pressure levels
        with the worse of the positive and negative DC bias if the variable
        offset is True and sound pressure levels without DC bias otherwise. The
        sound pressure level is calculated for each ground point used as input.
        """

        # dictionary for the rain rate correction (rain_rate: corr_factor)
        rain_corr_dicts = {
            0.1: -2.00,
            0.2: -1.40,
            0.3: -1.01,
            0.4: -0.73,
            0.5: -0.50,
            0.6: -0.30,
            0.7: -0.14,
            0.75: 0.00,
            0.8: 0.00,
            0.9: 0.13,
            1.0: 0.27,
            1.1: 0.37,
            1.2: 0.47,
            1.3: 0.57,
            1.4: 0.68,
            1.5: 0.78,
            1.6: 0.86,
            1.7: 0.94,
            1.8: 1.03,
            1.9: 1.11,
            2.0: 1.18,
            2.1: 1.25,
            2.2: 1.31,
            2.3: 1.38,
            2.4: 1.45,
            2.5: 1.50,
            2.6: 1.57,
            2.7: 1.63,
            2.8: 1.69,
            2.9: 1.75,
            3.0: 1.81,
            3.5: 2.06,
            4.0: 2.35,
            4.5: 2.55,
            5.0: 2.79,
            5.5: 2.98,
            6.0: 3.18,
            6.5: 3.37,
            7.0: 3.53,
            7.5: 3.72,
            7.7: 3.79,
            8.0: 3.89,
            8.5: 4.03,
            9.0: 4.19,
            9.5: 4.36,
            10.0: 4.52,
            11.0: 4.80,
            12.0: 5.08,
            13.0: 5.35,
            14.0: 5.67,
            15.0: 5.97,
            16.0: 6.22,
            17.0: 6.47,
            18.0: 6.71,
            19.0: 6.98,
            20.0: 7.26,
            21.0: 7.47,
            22.0: 7.69,
            23.0: 7.92,
            24.0: 8.14,
            25.0: 8.37,
            26.0: 8.56,
            27.0: 8.74,
            28.0: 8.93,
            29.0: 9.11,
            30.0: 9.28,
        }

        # get the right correction factor from the entered rain rate
        if 0.0 < rain_corr <= 30.0 and weather == "Foul":
            corr_factor = rain_corr_dicts.get(
                rain_corr,
                rain_corr_dicts[min(rain_corr_dicts.keys(), key=lambda k: abs(k - rain_corr))],
            )
        else:
            corr_factor = 0

        P_50 = []
        P_50_pos_offset = []
        P_50_neg_offset = []

        for system in self.systems:
            if system.system_type == "ac":
                for line in system.lines:
                    # rename the number of suubconductor variable for convenience
                    n_sc = line.num_con
                    # conversion from radius [m] to diameter [cm]
                    sc_d = line.con_radius * 2 * 100
                    bun_d = line.bundle_radius * 2 * 100

                    # define calculation constants
                    if n_sc == 1:
                        k = 7.5
                    elif n_sc == 2:
                        k = 2.6

                    # calculate the 6-dB gradient
                    if n_sc <= 8:
                        E_c = 24.4 / (sc_d**0.24)
                    elif n_sc > 8:
                        E_c = 24.4 / (sc_d**0.24) - (n_sc - 8) / 4

                    # calculate the heavy rain acoustic power in dBA above 1W/m
                    if n_sc < 3:
                        A_5 = (
                            20 * np.log10(n_sc)
                            + 44 * np.log10(sc_d)
                            - 665 / line.E_ac
                            + k
                            - 39.1
                            + an_unit
                            + (altitude - 300) / 300
                            + corr_factor
                        )
                        # calculate acoustic power with postive DC offset
                        A_5_pos_offset = (
                            20 * np.log10(n_sc)
                            + 44 * np.log10(sc_d)
                            - 665 / line.E_ac_pos_offset
                            + k
                            - 39.1
                            + an_unit
                            + (altitude - 300) / 300
                            + corr_factor
                        )
                        # calculate acoustic power with negative DC offset
                        A_5_neg_offset = (
                            20 * np.log10(n_sc)
                            + 44 * np.log10(sc_d)
                            - 665 / line.E_ac_neg_offset
                            + k
                            - 39.1
                            + an_unit
                            + (altitude - 300) / 300
                            + corr_factor
                        )
                    elif n_sc >= 3:
                        A_5 = (
                            20 * np.log10(n_sc)
                            + 44 * np.log10(sc_d)
                            - 665 / line.E_ac
                            + 22.9 * (n_sc - 1) * sc_d / bun_d
                            - 46.4
                            + an_unit
                            + (altitude - 300) / 300
                            + corr_factor
                        )
                        # calculate acoustic power with postive DC offset
                        A_5_pos_offset = (
                            20 * np.log10(n_sc)
                            + 44 * np.log10(sc_d)
                            - 665 / line.E_ac_pos_offset
                            + 22.9 * (n_sc - 1) * sc_d / bun_d
                            - 46.4
                            + an_unit
                            + (altitude - 300) / 300
                            + corr_factor
                        )
                        # calculate acoustic power with negative DC offset
                        # negative Trichel pulses emits lower noise level
                        # thus, 4dB is subtracted from negative offset
                        A_5_neg_offset = (
                            20 * np.log10(n_sc)
                            + 44 * np.log10(sc_d)
                            - 665 / line.E_ac_neg_offset
                            + 22.9 * (n_sc - 1) * sc_d / bun_d
                            - 46.4
                            - 4
                            + an_unit
                            + (altitude - 300) / 300
                            + corr_factor
                        )

                    #  calculate the correction factor for wet conductor level
                    if n_sc < 3:
                        delta_A = 8.2 - 14.2 * E_c / line.E_ac
                        delta_A_pos_offset = 8.2 - 14.2 * E_c / line.E_ac_pos_offset
                        delta_A_neg_offset = 8.2 - 14.2 * E_c / line.E_ac_neg_offset
                    elif n_sc >= 3:
                        delta_A = 10.4 - 14.2 * E_c / line.E_ac + 8 * (n_sc - 1) * sc_d / bun_d
                        delta_A_pos_offset = (
                            10.4 - 14.2 * E_c / line.E_ac_pos_offset + 8 * (n_sc - 1) * sc_d / bun_d
                        )
                        delta_A_neg_offset = (
                            10.4 - 14.2 * E_c / line.E_ac_neg_offset + 8 * (n_sc - 1) * sc_d / bun_d
                        )

                    # calculate the measurable rain acoustic power in dB
                    A_50 = A_5 + delta_A
                    A_50_pos_offset = A_5_pos_offset + delta_A_pos_offset
                    A_50_neg_offset = A_5_neg_offset + delta_A_neg_offset

                    # calculate the distance between the line and ground points
                    dist = np.sqrt(
                        np.add(
                            np.square(np.subtract(ground_points, line.line_x)),
                            np.square(line.line_y),
                        )
                    )

                    # calculate the sound pressure levels in dBA
                    P_50_iter = np.subtract(
                        A_50 + 114.3,
                        np.add(np.multiply(10, np.log10(dist)), np.multiply(0.02, dist)),
                    )
                    P_50_pos_offset_iter = np.subtract(
                        A_50_pos_offset + 114.3,
                        np.add(np.multiply(10, np.log10(dist)), np.multiply(0.02, dist)),
                    )
                    P_50_neg_offset_iter = np.subtract(
                        A_50_neg_offset + 114.3,
                        np.add(np.multiply(10, np.log10(dist)), np.multiply(0.02, dist)),
                    )

                    # subtract 25 dB for fair weather
                    if weather == "Fair":
                        P_50_iter = np.subtract(P_50_iter, 25)
                        P_50_pos_offset_iter = np.subtract(P_50_pos_offset_iter, 25)
                        P_50_neg_offset_iter = np.subtract(P_50_neg_offset_iter, 25)

                    P_50.append(P_50_iter)
                    P_50_pos_offset.append(P_50_pos_offset_iter)
                    P_50_neg_offset.append(P_50_neg_offset_iter)

                    # save the acoustic power as a line variable
                    if not offset:
                        line.AC_EPRI_L_w50 = A_50
                    else:
                        line.AC_EPRI_L_w50 = np.maximum(A_50_pos_offset, A_50_neg_offset)
                    if weather == "Fair":
                        line.AC_EPRI_L_w50 -= 25

        # sum the audible noise from all lines for each ground point
        P_50_sum = 10 * np.log10(np.sum(np.power(10, np.divide(P_50, 10)), axis=0))
        P_50_pos_offset_sum = 10 * np.log10(
            np.sum(np.power(10, np.divide(P_50_pos_offset, 10)), axis=0)
        )
        P_50_neg_offset_sum = 10 * np.log10(
            np.sum(np.power(10, np.divide(P_50_neg_offset, 10)), axis=0)
        )

        if not offset:
            return P_50_sum
        if np.max(P_50_pos_offset_sum) > np.max(P_50_neg_offset_sum):
            return P_50_pos_offset_sum
        return P_50_neg_offset_sum

    def calc_AN_AC_BPA(self, ground_points, weather, offset, an_unit, altitude, rain_corr):
        """This method calculates the audible noise of AC lines according to the
        empirical formula defined by BPA.

        input variable(s):

        * ground_points: Numpy array containing x-coordinates of ground points
        * weather:
            * Foul: default weather condition for the AC BPA calculation
            * Fair: reduces the audible noise by 25dB
        * offset: boolean value which returns offset audible noise value if true
        * an_unit: offset for the acoustic power calculation depending on unit chosen
        * altitude: audible noise altitude correction in meter
        * rain_corr: the rain rate for the inclusion of rain factor correction in calculation

        The return value is a Numpy array containing the sound pressure levels
        with the worse of the positive and negative DC bias if the variable
        offset is True and sound pressure levels without DC bias otherwise. The
        sound pressure level is calculated for each ground point used as input.
        """

        # dictionary for the rain rate correction (rain_rate: corr_factor)
        rain_corr_dicts = {
            0.1: -2.00,
            0.2: -1.40,
            0.3: -1.01,
            0.4: -0.73,
            0.5: -0.50,
            0.6: -0.30,
            0.7: -0.14,
            0.75: 0.00,
            0.8: 0.00,
            0.9: 0.13,
            1.0: 0.27,
            1.1: 0.37,
            1.2: 0.47,
            1.3: 0.57,
            1.4: 0.68,
            1.5: 0.78,
            1.6: 0.86,
            1.7: 0.94,
            1.8: 1.03,
            1.9: 1.11,
            2.0: 1.18,
            2.1: 1.25,
            2.2: 1.31,
            2.3: 1.38,
            2.4: 1.45,
            2.5: 1.50,
            2.6: 1.57,
            2.7: 1.63,
            2.8: 1.69,
            2.9: 1.75,
            3.0: 1.81,
            3.5: 2.06,
            4.0: 2.35,
            4.5: 2.55,
            5.0: 2.79,
            5.5: 2.98,
            6.0: 3.18,
            6.5: 3.37,
            7.0: 3.53,
            7.5: 3.72,
            7.7: 3.79,
            8.0: 3.89,
            8.5: 4.03,
            9.0: 4.19,
            9.5: 4.36,
            10.0: 4.52,
            11.0: 4.80,
            12.0: 5.08,
            13.0: 5.35,
            14.0: 5.67,
            15.0: 5.97,
            16.0: 6.22,
            17.0: 6.47,
            18.0: 6.71,
            19.0: 6.98,
            20.0: 7.26,
            21.0: 7.47,
            22.0: 7.69,
            23.0: 7.92,
            24.0: 8.14,
            25.0: 8.37,
            26.0: 8.56,
            27.0: 8.74,
            28.0: 8.93,
            29.0: 9.11,
            30.0: 9.28,
        }

        # get the right correction factor from the entered rain rate
        if 0.0 < rain_corr <= 30.0 and weather == "Foul":
            corr_factor = rain_corr_dicts.get(
                rain_corr,
                rain_corr_dicts[min(rain_corr_dicts.keys(), key=lambda k: abs(k - rain_corr))],
            )
        else:
            corr_factor = 0

        L_50 = []
        L_50_offset = []

        for system in self.systems:
            if system.system_type == "ac":
                for line in system.lines:
                    # rename the number of subconductor variable for convenience
                    n_sc = line.num_con
                    # conversion from radius [m] to diameter [cm]
                    sc_d = line.con_radius * 2 * 100

                    # define calculation constants
                    if 0 < n_sc < 3:
                        k = 0
                        AN_0 = -115.4
                    elif n_sc >= 3:
                        k = 26.4
                        AN_0 = -128.4

                    # calculate the heavy rain acoustic power in dBA above 1W/m
                    L_w50 = (
                        120 * np.log10(line.E_ac)
                        + k * np.log10(n_sc)
                        + 55 * np.log10(sc_d)
                        + AN_0
                        - 114.3
                        + an_unit
                        + (altitude - 300) / 300
                    ) + corr_factor
                    # calculate the acoustic power with positive DC offset
                    # in contrast to the EPRI method, the negative offset
                    # is neglected in the BPA method.
                    L_w50_pos_offset = (
                        120 * np.log10(line.E_ac_pos_offset)
                        + k * np.log10(n_sc)
                        + 55 * np.log10(sc_d)
                        + AN_0
                        - 114.3
                        + an_unit
                        + (altitude - 300) / 300
                    ) + corr_factor

                    # calculate the distance between the line and ground points
                    dist = np.sqrt(
                        np.add(
                            np.square(np.subtract(ground_points, line.line_x)),
                            np.square(line.line_y),
                        )
                    )

                    # calculate the sound pressure levels
                    L_50_iter = np.subtract(L_w50 + 114.3, np.multiply(11.4, np.log10(dist)))
                    # calculate the sound pressure levels with positive offset
                    L_50_offset_iter = np.subtract(
                        L_w50_pos_offset + 114.3, np.multiply(11.4, np.log10(dist))
                    )

                    # subtract 25 dB for fair weather
                    if weather == "Fair":
                        L_50_iter = np.subtract(L_50_iter, 25)
                        L_50_offset_iter = np.subtract(L_50_offset_iter, 25)

                    # calculate the audible noise in dBA above 20 * 10e-6 Pa
                    L_50.append(L_50_iter)
                    L_50_offset.append(L_50_offset_iter)

                    # save the acoustic power as a line variable
                    if not offset:
                        line.AC_BPA_L_w50 = L_w50
                    else:
                        line.AC_BPA_L_w50 = L_w50_pos_offset
                    if weather == "Fair":
                        line.AC_BPA_L_w50 -= 25

        # sum the audible noise from all lines for each ground point
        L_50_sum = 10 * np.log10(np.sum(np.power(10, np.divide(L_50, 10)), axis=0))
        L_50_offset_sum = 10 * np.log10(np.sum(np.power(10, np.divide(L_50_offset, 10)), axis=0))

        if not offset:
            return L_50_sum
        return L_50_offset_sum

    def calc_AN_DC_EPRI(self, ground_points, weather, season, an_unit, altitude):
        """This method calculates the audible noise of DC lines according to the
        empirical formula defined by EPRI.

        input variable(s):

        * ground_points: Numpy array containing x-coordinates of ground points
        * weather:
            * Fair: default weather condition for the DC EPRI calculation
            * Foul: reduces the audible noise by 6dB
        * season:
            * Summer: default seasonal condition for the DC EPRI calculation
            * Winter: reduces the audible noise by 4dB
            * Fall/Spring: reduces the audible noise by 2dB
        * an_unit: offset for the acoustic power calculation depending on unit chosen
        * altitude: audible noise altitude correction in meter

        The return value is a Numpy array containing the sound pressure level
        calculated at each ground point used as input.
        """

        P_50 = []
        P_5 = []

        for system in self.systems:
            if system.system_type in ["dc", "dc_bipol"]:
                for line in system.lines:
                    if line.line_type == "dc_neut":
                        continue

                    # rename the number of suubconductor variable for convenience
                    n_sc = line.num_con
                    # conversion from radius [m] to diameter [cm]
                    sc_d = line.con_radius * 2 * 100

                    # define calculation constants
                    if n_sc == 1:
                        k = 7.5
                    elif n_sc == 2:
                        k = 2.6
                    elif n_sc >= 3:
                        k = 0

                    # calculate the acoustic power
                    L_50 = (
                        -57.4
                        + k
                        + 124 * np.log10(np.abs(line.E_dc_rip / 25))
                        + 25 * np.log10(sc_d / 4.45)
                        + 18 * np.log10(n_sc / 2)
                        + an_unit
                        + (altitude - 300) / 300
                    )
                    if line.E_dc < 0:
                        L_50 = L_50 - 8

                    # calculate the distance between the line and ground points
                    dist = np.sqrt(
                        np.add(
                            np.square(ground_points - line.line_x),
                            np.square(line.line_y),
                        )
                    )

                    # calculate the sound pressure level in dBA
                    P_50_i = np.subtract(
                        L_50 + 114.3,
                        10.0 * np.log10(dist) + 0.02 * dist,
                    )

                    # take into account the season
                    season_offset = {"Winter": -4.0, "Fall/Spring": -2.0}
                    P_50_i += season_offset.get(season, 0.0)

                    # subtract 6 dB for foul weather
                    if weather == "Foul":
                        P_50_i = P_50_i - 6.0

                    P_50.append(P_50_i)

                    P_5_i = P_50_i - 6.0
                    P_5.append(P_5_i)

                    # save the acoustic power as a line variable
                    line.DC_EPRI_L_w50 = L_50
                    line.DC_EPRI_L_w50 += season_offset.get(season, 0.0)
                    if weather == "Foul":
                        line.DC_EPRI_L_w50 -= 6

        # sum the audible noise from all lines for each ground point
        return 10 * np.log10(np.sum(np.power(10, np.divide(P_50, 10)), axis=0))

    def calc_AN_DC_BPA(self, ground_points, weather, season, an_unit, altitude):
        """This method calculates the audible noise of DC lines according to the
        empirical formula defined by BPA.

        input variable(s):

        * ground_points: Numpy array containing x-coordinates of ground points
        * weather:
            * Fair: default weather condition for the DC BPA calculation
            * Foul: reduces the audible noise by 6dB
        * season:
            * Fall/Spring: default seasonal condition for the DC BPA calculation
            * Summer: increases the audible noise by 2dB
            * Winter: reduces the audible noise by 2dB
        * an_unit: offset for the acoustic power calculation depending on unit chosen
        * altitude: audible noise altitude correction in meter

        The return value is a Numpy array containing the sound pressure level
        calculated at each ground point used as input.
        """

        L_50 = []
        season_enum = Season(season.lower())  # TODO to be removed after new SettingsParser

        for system in self.systems:
            if system.system_type in {"dc", "dc_bipol"}:
                for line in system.lines:
                    if line.line_type == "dc_neut":
                        continue

                    # rename the number of suubconductor variable for convenience
                    n_sc = line.num_con
                    # conversion from radius [m] to diameter [mm]
                    sc_d = line.con_radius * 2 * 1000

                    # calculate equivalent diameter
                    if 0 < n_sc < 3:
                        d_eq = sc_d
                    elif n_sc >= 3:
                        d_eq = sc_d * 0.66 * n_sc**0.64

                    # calculate the acoustic power
                    L_w50 = (
                        -127.6
                        + 86 * np.log10(np.abs(line.E_dc_rip))
                        + 40 * np.log10(d_eq)
                        - 114.3
                        + an_unit
                        + (altitude - 300) / 300
                    )
                    if line.E_dc < 0:
                        L_w50 = L_w50 - 8

                    # calculate the distance between the line and ground points
                    dist = np.sqrt(
                        np.add(
                            np.square(np.subtract(ground_points, line.line_x)),
                            np.square(line.line_y),
                        )
                    )

                    L_50_i = np.subtract(L_w50 + 114.3 - 5.8, np.multiply(11.4, np.log10(dist)))

                    # take into account the season

                    season_correction = AudibleNoiseCorrections.season_dc_offset_bpa(season_enum)
                    L_50_i = L_50_i + season_correction

                    # subtract 6 dB for foul weather
                    if weather == "Foul":
                        L_50_i = L_50_i - 6.0

                    # calculate the sound pressure levels in dBA
                    L_50.append(L_50_i)

                    # save the acoustic power as a line variable
                    line.DC_BPA_L_w50 = L_w50 - 5.8 + season_correction
                    if weather == "Foul":
                        line.DC_BPA_L_w50 -= 6

        # sum the audible noise from all lines for each ground point
        return 10 * np.log10(np.sum(np.power(10, np.divide(L_50, 10)), axis=0))

    def calc_AN_DC_CRIEPI(self, ground_points, an_unit):
        """This method calculates the audible noise of DC lines according to the
        empirical formula defined by BPA.

        input variable(s):

        * ground_points: Numpy array containing x-coordinates of ground points
        * an_unit: offset for the acoustic power calculation depending on unit chosen

        The return value is a Numpy array containing the sound pressure level
        calculated at each ground point used as input.
        """

        L_50 = []

        for system in self.systems:
            if system.system_type in ["dc", "dc_bipol"]:
                for line in system.lines:
                    if line.line_type == "dc_neut":
                        continue

                    # rename the number of suubconductor variable for convenience
                    n_sc = line.num_con
                    # conversion from radius [m] to diameter [cm]
                    sc_d = line.con_radius * 2 * 100

                    if line.line_type == "dc_pos":
                        x_pos = line.line_x
                        y_pos = line.line_y
                    elif line.line_type == "dc_neg":
                        x_neg = line.line_x
                        y_neg = line.line_y

                for line in system.lines:
                    if line.line_type == "dc_neut":
                        continue

                    # calculate equivalent diameter
                    dist_bipol = np.sqrt((x_pos - x_neg) ** 2 + (y_pos - y_neg) ** 2)
                    g_50 = (
                        np.log10(n_sc) / 91
                        + np.log10(sc_d) / 19
                        + (2 * dist_bipol**2) ** -1
                        + 151**-1
                    ) ** -1
                    g_60 = (
                        np.log10(n_sc) / 71
                        + np.log10(sc_d) / 21
                        + (2 * dist_bipol**2) ** -1
                        + 1906**-1
                    ) ** -1

                    # calculate the acoustic power
                    L_w50 = (
                        10 * (g_60 / (g_60 - g_50)) * (1 - g_50 / np.abs(line.E_dc_rip))
                        + 50
                        - 114.3
                        + an_unit
                    )
                    if line.E_dc < 0:
                        L_w50 = L_w50 - 8

                    # calculate the distance between the line and ground points
                    dist = np.sqrt(
                        np.add(
                            np.square(np.subtract(ground_points, line.line_x)),
                            np.square(line.line_y),
                        )
                    )

                    # calculate the sound pressure levels in dBA
                    L_50.append(np.subtract(L_w50 + 114.3, np.multiply(10, np.log10(dist))))

                    # save the acoustic power as a line variable
                    line.DC_CRIEPI_L_w50 = L_w50

        # sum the audible noise from all lines for each ground point
        return 10 * np.log10(np.sum(np.power(10, np.divide(L_50, 10)), axis=0))

    def save_tower_config(self, file_name):
        """This method saves the tower configuration as a JSON file in the
        specified path in file_name.
        """

        tow_param = []
        # add parameters belonging to the individual systems
        for system_idx, system in enumerate(self.systems):
            lines = []
            for line in system.lines:
                lines.append(
                    {
                        "line_type": line.line_type,
                        "line_x": line.line_x,
                        "line_y": line.line_y,
                        "con_radius": line.con_radius,
                        "num_con": line.num_con,
                        "bundle_radius": line.bundle_radius,
                        "con_angle_offset": line.con_angle_offset,
                    }
                )

            tow_param.append(
                {
                    "system_idx": system_idx,
                    "system_type": system.system_type,
                    "voltage": system.voltage,
                    "current": system.current,
                    "lines": lines,
                }
            )

        try:
            # write the parameters into a text file
            with open(file_name, "w", encoding="utf-8") as f:
                json.dump(tow_param, f, indent=4)
        except PermissionError as e:
            print(e)

    def load_tower_config(self, file_name):
        """This method load the tower geometry from a JSON file in the specified
        path given in file_name.
        """

        try:
            # load the tower configuration from a JSON file
            with open(file_name, "r", encoding="utf-8") as f:
                tow_param = json.load(f)
        except PermissionError as e:
            print(e)
            return

        # Delete the current systems list and create a new list
        del self.systems[:]
        self.systems = []

        for system_param in tow_param:
            system = System(
                system_param["system_type"],
                system_param["voltage"],
                system_param["current"],
            )
            for line_param in system_param["lines"]:
                line = Line(
                    line_param["line_type"],
                    line_param["line_x"],
                    line_param["line_y"],
                    line_param["con_radius"],
                    line_param["num_con"],
                    line_param["bundle_radius"],
                    line_param["con_angle_offset"],
                )
                system.add_line(line)
            self.add_system(system)
