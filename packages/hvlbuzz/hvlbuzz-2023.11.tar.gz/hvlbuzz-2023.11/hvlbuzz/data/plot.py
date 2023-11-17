"""Ui components for plots."""

import os

from typing import Any
from collections.abc import Callable

from kivy.core.window import Window
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.logger import Logger

# Import NumPy and Matplotlib for mathematical operations and plotting
# The Kivy backend for Matplotlib is also included
import numpy as np
import matplotlib

from matplotlib.collections import CircleCollection
import matplotlib.pyplot as plt
from kivy_garden.matplotlib.backend_kivy import FigureCanvasKivy, NavigationToolbar2Kivy

# Import from the GUI utilities file
from ..util.settingsparser import SettingsParser
from ..util.gui_tools import move_tooltip, paint_blue, paint_white
from .. import MODULE_DIR

matplotlib.use("module://kivy_garden.matplotlib.backend_kivy")


class ToolTip(Label):
    """The implementation of ToolTip can be found in the buzz.kv file"""


class ToolbarButton(ButtonBehavior, Image):
    """Instances of ToolbarButton are images which behave as a button.

    initialization variable(s):

    * text: the text to be shown on the button ToolTip
    """

    bind: Callable[[Any], Any]

    def __init__(self, text, **kwargs):
        Window.bind(mouse_pos=self.on_mouse_pos)
        super().__init__(**kwargs)

        # initialize the ToolTip
        self.tooltip = ToolTip(text=text)

    def paint_bg_blue(self):
        """This method paints the button background blue."""
        paint_blue(self)

    def paint_bg_white(self):
        """This method paints the button background white."""
        paint_white(self)

    def on_mouse_pos(self, *args):
        """This method shows and closes the tooltip depending on mouse position."""
        move_tooltip(self, pos=args[1])

    def close_tooltip(self, *_args):
        """This method removes the tooltip widget from the window."""
        Window.remove_widget(self.tooltip)

    def display_tooltip(self, *_args):
        """This method adds the tooltip widget to the window."""
        Window.add_widget(self.tooltip)


class BuzzPlotToolbar(NavigationToolbar2Kivy):
    """BuzzPlotToolbar adds Matplotlib figure utilities to the BuzzPlot
    instance. The available figure utilities are:

    * Home: switch to the first view
    * Backward: traverse to the last view
    * Forward: traverse to the next view
    * Pan: pan the plot
    * Zoom: zoom to the specified rectangle

    initialization variable(s):

    * canvas: the BuzzPlot canvas for which the toolbar should be created

    Each utility is bound to a ToolbarButton which exists in a BoxLayout.

    The pan and zoom utilities are toggle buttons. Once they are toggled on,
    they will stay active until the buttons are toggled off. The background of
    these buttons will stay blue as long as they are active. The pan button
    will be inactivated when the zoom button is toggled active and vice versa.
    """

    def __init__(self, canvas, **_kwargs):
        # set the size of the BoxLayout
        self.layout = BoxLayout(size_hint=(1, 0.1))
        super().__init__(canvas)
        self.home_btn = None
        self.back_btn = None
        self.forward_btn = None
        self.zoom_btn = None
        self.pan_btn = None
        # initializes the toggle status of the pan and zoom buttons
        self.pan_active = False
        self.zoom_active = False
        self._init_toolbar()

    def _init_toolbar(self):
        """This method initializes the toolbar buttons with the corresponding
        images and texts. The button bindings to the class methods are also
        set in this method.
        """

        # Get the path to the Matplotlib toolbar images
        image_dir = os.path.join(MODULE_DIR, "static", "images")

        # creates the home button
        home_btn_image = os.path.join(image_dir, "home.png")
        self.home_btn = ToolbarButton(source=home_btn_image, text="Home")
        self.home_btn.bind(on_press=self.home_press)
        self.home_btn.bind(on_release=self.home_release)
        self.layout.add_widget(self.home_btn)

        # creates the back button
        back_btn_image = os.path.join(image_dir, "back.png")
        self.back_btn = ToolbarButton(source=back_btn_image, text="Back")
        self.back_btn.bind(on_press=self.back_press)
        self.back_btn.bind(on_release=self.back_release)
        self.layout.add_widget(self.back_btn)

        # creates the forward button
        forward_btn_image = os.path.join(image_dir, "forward.png")
        self.forward_btn = ToolbarButton(source=forward_btn_image, text="Forward")
        self.forward_btn.bind(on_press=self.forward_press)
        self.forward_btn.bind(on_release=self.forward_release)
        self.layout.add_widget(self.forward_btn)

        # creates the pan button
        pan_btn_image = os.path.join(image_dir, "move.png")
        self.pan_btn = ToolbarButton(source=pan_btn_image, text="Pan")
        self.pan_btn.bind(on_press=self.pan_press)
        self.pan_btn.bind(on_release=self.pan_release)
        self.layout.add_widget(self.pan_btn)

        # creates the zoom button
        zoom_btn_image = os.path.join(image_dir, "zoom_to_rect.png")
        self.zoom_btn = ToolbarButton(source=zoom_btn_image, text="Zoom")
        self.zoom_btn.bind(on_press=self.zoom_press)
        self.zoom_btn.bind(on_release=self.zoom_release)
        self.layout.add_widget(self.zoom_btn)

    def home_press(self, _event):
        """This method is prompted on the press of the home button."""
        self.home_btn.paint_bg_blue()

    def home_release(self, _event):
        """This method is prompted on the release of the home button."""
        self.home_btn.paint_bg_white()
        self.home()

    def back_press(self, _event):
        """This method is prompted on the press of the back button."""
        self.back_btn.paint_bg_blue()

    def back_release(self, _event):
        """This method is prompted on the release of the back button."""
        self.back_btn.paint_bg_white()
        self.back()

    def forward_press(self, _event):
        """This method is prompted on the press of the forward button."""
        self.forward_btn.paint_bg_blue()

    def forward_release(self, _event):
        """This method is prompted on the release of the forward button."""
        self.forward_btn.paint_bg_white()
        self.forward()

    def pan_press(self, _event):
        """This method is prompted on the press of the pan button."""
        if self.pan_active:
            self.pan_btn.paint_bg_white()
        else:
            self.pan_btn.paint_bg_blue()
            self.zoom_btn.paint_bg_white()
        self.pan_active = not self.pan_active

    def pan_release(self, _event):
        """This method is prompted on the release of the pan button."""
        self.pan()

    def zoom_press(self, _event):
        """This method is prompted on the press of the zoom button."""
        if self.zoom_active:
            self.zoom_btn.paint_bg_white()
        else:
            self.zoom_btn.paint_bg_blue()
            self.pan_btn.paint_bg_white()
        self.zoom_active = not self.zoom_active

    def zoom_release(self, _event):
        """This method is prompted on the release of the zoom button."""
        self.zoom()


class BuzzPlot(BoxLayout):
    """BuzzPlot is a BoxLayout that contains the Matplotlib plot and the
    corresponding BuzzPlotToolbar. The functions which are responsible for the
    plotting of tower geometries, audible noise level and annotating electric
    field strength is also contained in this class.

    initialization variable(s):

    * tower: is the instance of Tower class on which plotting operations
            are to be done. All calculations are contained within the Tower
            class definition. The BuzzPlot instance receives the numerical
            results and create the plot accordingly.

    The plotting settings, such as color and size, can be adjusted in the
    Kivy settings screen.
    """

    def __init__(self, tower, **kwargs):
        super().__init__(**kwargs)

        # Change the BoxLayout orientation to vertical
        self.orientation = "vertical"

        # Tower instance which calculates the plot data
        self.tower = tower

        # Create a Matplotlib figure canvas and its corresponding toolbar
        fig = plt.Figure()
        ax = fig.add_axes([0.1, 0.1, 0.6, 0.8])
        self.fig = fig
        self.ax = ax
        self.distance_axis = ax.twinx()
        self.distance_axis.yaxis.set_visible(False)
        self.fig_canvas = FigureCanvasKivy(fig)
        self.toolbar = BuzzPlotToolbar(self.fig_canvas)
        self.add_widget(self.fig_canvas)
        self.add_widget(self.toolbar.layout)

        # initialize a parser for the settings .ini file
        self.settings = SettingsParser()

        self.an_ac_epri = []
        self.an_ac_bpa = []
        self.an_dc_bpa = []
        self.an_dc_criepi = []
        self.an_dc_epri = []
        self.an_ground_points = np.array([])
        self.ef_ground_points = np.array([])
        self.ef_height_above_ground = 0.0
        self.mf_ground_points = np.array([])
        self.mf_height_above_ground = 0.0

        self._fontsize = 12

    def _set_ylabel(self, ax, ytext):
        ax.legend(bbox_to_anchor=(1.1, 0), loc=3, borderaxespad=0.0, fontsize=self._fontsize)
        ax.set_xlabel("Lateral distance from line axis in m", size=self._fontsize)
        ax.set_ylabel(ytext, size=self._fontsize, rotation=0, va="bottom", ha="left")
        ax.yaxis.set_label_coords(0, 1.01)
        ax.yaxis.set_visible(True)
        ax.tick_params(axis="both", which="major", labelsize=self._fontsize)

    def _msg_line_collision(self, ax):
        ax.text(
            0.5,
            0.5,
            "check for line collision",
            horizontalalignment="center",
            verticalalignment="center",
            transform=ax.transAxes,
        )

    def reset_settings_parser(self):
        """This method prompts the settings parser to reload configurations from
        the buzz.ini file"""
        self.settings.reset()

    def export_canvas_to_png(self, path, filename):
        """This method saves the current plot as a PNG image."""
        try:
            path = os.path.join(path, filename)
            # set the size of the image for better quality
            self.fig.set_size_inches(7, 7)
            self.fig.savefig(path)
        except PermissionError as e:
            print(e)

    def plot_tower_geometry(self):
        """This method plots the conductor midpoints as a scatter plot."""
        # clear primary axis
        self.distance_axis.clear()

        # create the scatter plots
        for system in self.tower.systems:
            for line in system.lines:
                # Get the colors of the scatter from the settings parser
                color = self.settings.get_con_color(line.line_type)[0]
                radius_mult = self.settings.get_radius_mult()
                con_x = []
                con_y = []
                for i in range(line.num_con):
                    con_x.append(
                        (
                            line.line_x
                            + radius_mult
                            * line.bundle_radius
                            * np.cos(
                                2 * np.pi * i / line.num_con + line.con_angle_offset * np.pi / 180
                            )
                        )
                    )
                    con_y.append(
                        line.line_y
                        + radius_mult
                        * line.bundle_radius
                        * np.sin(2 * np.pi * i / line.num_con + line.con_angle_offset * np.pi / 180)
                    )
                self.distance_axis.scatter(con_x, con_y, color=color)

        # set the y-axis limits
        if not self.settings.get_tg_auto_axis():
            ymin = self.settings.get_tg_lower_axis()
            ymax = self.settings.get_tg_upper_axis()
            self.distance_axis.set_ylim(ymin, ymax)
        else:
            self.distance_axis.set_ylim(None, None)

        # adjust the legends and labels of the figure
        scatter_handles, scatter_labels = self.get_scatter_label()
        self.distance_axis.legend(
            scatter_handles,
            scatter_labels,
            bbox_to_anchor=(1.1, 1),
            loc=2,
            borderaxespad=0.0,
            fontsize=12,
        )

        # draw the changes to the plot
        self.fig_canvas.draw_idle()

    def get_scatter_label(self):
        """This method generates the appropriate legends for the tower geometry
        scatter plot.
        """
        # create customs artists for the legend
        scatter_handles = []
        line_types = ["ac_r", "dc_pos", "dc_neg", "dc_neut", "gnd"]
        for line_type in line_types:
            size = [20]
            color = self.settings.get_con_color(line_type)[0]
            artist = CircleCollection(size, facecolors=color)
            scatter_handles.append(artist)
        # create the corresponding string labels
        scatter_labels = ["AC", "DC Positive", "DC Negative", "DC Neutral", "Ground"]
        return scatter_handles, scatter_labels

    def plot_audible_noise(self):
        """This method plots the audible noise level according to the following
        calculations:

        * AC EPRI
        * AC BPA
        * DC EPRI
        * DC BPA
        * DC CRIEPI

        The audible noise plot will overlap the tower geometry scatter plot but
        has its value shown on a secondary y-axis. The corresponding legend
        of the audible noise plot will also be added.
        """

        # clear secondary axis
        self.ax.clear()
        self.an_ac_epri = []
        self.an_ac_bpa = []
        self.an_dc_bpa = []
        self.an_dc_criepi = []
        self.an_dc_epri = []
        # get the ground points
        start, end, n = self.settings.get_an_ground_points()
        self.an_ground_points = np.linspace(start, end, num=n)
        # get the number of contour points
        self.tower.set_num_contour(self.settings.get_ef_num_contour())
        # calculate the conductor surface gradient
        status = self.tower.calc_ave_max_conductor_surface_gradient()

        # print text if calculation is unsuccessful due to line collision
        if not status:
            self._msg_line_collision(self.ax)
            # draw changes to the plot
            self.fig_canvas.draw_idle()
            # log the error
            Logger.exception("Line Collision: surface gradient calculation aborted.")
            return

        system_types = {system.system_type for system in self.tower.systems}

        # AN always in dBA for all plots (in app and exported) and csv
        altitude = self.settings.get_an_altitude()
        if "ac" in system_types:
            if self.settings.get_ac_epri_bool():
                self.plot_an_ac_epri(altitude)

            if self.settings.get_ac_bpa_bool():
                self.plot_an_ac_bpa(altitude)

        if "dc" in system_types or "dc_bipol" in system_types:
            if self.settings.get_dc_epri_bool():
                self.plot_an_dc_epri(altitude)

            if self.settings.get_dc_bpa_bool():
                self.plot_an_dc_bpa(altitude)

            if self.settings.get_dc_criepi_bool():
                self.plot_an_dc_criepi()

        # set the y-axis limits
        if not self.settings.get_an_auto_axis():
            self.ax.set_ylim(
                ymin=self.settings.get_an_lower_axis(),
                ymax=self.settings.get_an_upper_axis(),
            )
        else:
            self.ax.set_ylim(None, None)

        # adjust the legends and labels of the figure
        self._set_ylabel(self.ax, "Audible Noise Level in dBA")

        # draw the changes to the plot
        self.fig_canvas.draw_idle()

    def plot_an_ac_epri(self, altitude: float) -> None:
        """Plots the audible noise level according to AC EPRI."""
        # Calculate AC EPRI audible noise
        weather = self.settings.get_ac_epri_weather()
        offset = self.settings.get_ac_epri_offset()
        rain_corr = self.settings.get_ac_epri_rain_corr()

        self.an_ac_epri = self.tower.calc_AN_AC_EPRI(
            self.an_ground_points,
            weather,
            offset,
            an_unit=0,
            altitude=altitude,
            rain_corr=rain_corr,
        )

        self.ax.plot(
            self.an_ground_points,
            self.an_ac_epri,
            label="AC EPRI",
            color="midnightblue",
            linewidth=4,
        )

        Logger.info(
            """AN AC EPRI: DC Offset = %s
AN AC EPRI: Weather = %s
AN AC EPRI: Max sound pressure level = %s dBA
Rain Correction: Raw Input = %s""",
            offset,
            weather,
            str(np.max(self.an_ac_epri)),
            str(rain_corr),
        )

    def plot_an_ac_bpa(self, altitude: float) -> None:
        """Plots the audible noise level according to AC BPA."""
        # Calculate AC BPA audible noise
        weather = self.settings.get_ac_bpa_weather()
        offset = self.settings.get_ac_bpa_offset()
        rain_corr = (
            self.settings.get_ac_epri_rain_corr()
        )  # originally rain_corr was only used for EPRI

        self.an_ac_bpa = self.tower.calc_AN_AC_BPA(
            self.an_ground_points,
            weather,
            offset,
            an_unit=0,
            altitude=altitude,
            rain_corr=rain_corr,
        )

        self.ax.plot(
            self.an_ground_points,
            self.an_ac_bpa,
            label="AC BPA",
            color="blue",
            linewidth=4,
        )

        Logger.info(
            """AN AC BPA: DC Offset = %s
AN AC BPA: Weather = %s
AN AC BPA: Max sound pressure level = %s dBA""",
            offset,
            weather,
            np.max(self.an_ac_bpa),
        )

    def plot_an_dc_epri(self, altitude: float) -> None:
        """Plots the audible noise level according to DC EPRI."""
        # Calculate DC EPRI audible noise
        weather = self.settings.get_dc_epri_weather()
        season = self.settings.get_dc_epri_season()

        self.an_dc_epri = self.tower.calc_AN_DC_EPRI(
            self.an_ground_points,
            weather,
            season,
            an_unit=0,
            altitude=altitude,
        )

        self.ax.plot(
            self.an_ground_points,
            self.an_dc_epri,
            label="DC EPRI",
            color="firebrick",
            linewidth=4,
        )

        Logger.info(
            """AN DC EPRI: Weather = %s
AN DC EPRI: Season = %s
AN DC EPRI: Max sound pressure level = %s dBA""",
            weather,
            season,
            str(np.max(self.an_dc_epri)),
        )

    def plot_an_dc_bpa(self, altitude: float) -> None:
        """Plots the audible noise level according to DC BPA."""
        # Calculate DC BPA audible noise
        weather = self.settings.get_dc_bpa_weather()
        season = self.settings.get_dc_bpa_season()

        self.an_dc_bpa = self.tower.calc_AN_DC_BPA(
            self.an_ground_points,
            weather,
            season,
            an_unit=0,
            altitude=altitude,
        )
        self.ax.plot(
            self.an_ground_points,
            self.an_dc_bpa,
            label="DC BPA",
            color="orangered",
            linewidth=4,
        )

        Logger.info(
            """AN DC BPA: Weather = %s
AN DC BPA: Season = %s
AN DC BPA: Max sound pressure level = %s dBA""",
            weather,
            season,
            str(np.max(self.an_dc_bpa)),
        )

    def plot_an_dc_criepi(self) -> None:
        """Plots the audible noise level according to DC CRIEPI."""
        # Calculate DC CRIEPI audible noise
        self.an_dc_criepi = self.tower.calc_AN_DC_CRIEPI(self.an_ground_points, an_unit=0)

        self.ax.plot(
            self.an_ground_points,
            self.an_dc_criepi,
            label="DC CRIEPI",
            color="darkorange",
            linewidth=4,
        )

        Logger.info(
            "AN DC CRIEPI: Max sound pressure level = %s %s",
            str(np.max(self.an_dc_criepi)),
            "dBA",
        )

    def plot_electric_field(self):
        """This method plots the electric field on the ground level.

        The electric field plot will overlap the tower geometry scatter plot but
        has its value shown on a secondary y-axis. The corresponding legend
        of the electric field plot will also be added.
        """
        # clear secondary axis
        self.ax.clear()

        # get the ground points
        start, end, n = self.settings.get_ef_ground_points()
        self.ef_ground_points = np.linspace(start, end, num=n)
        self.ef_height_above_ground = self.settings.get_ef_height_above_ground()
        # get the number of contour points
        self.tower.set_num_contour(self.settings.get_ef_num_contour())
        # calculate the electric field
        status = self.tower.calc_electric_field(self.ef_ground_points, self.ef_height_above_ground)

        # print text if calculation is unsuccessful due to line collision
        if not status:
            self._msg_line_collision(self.ax)
            # draw changes to the plot
            self.fig_canvas.draw_idle()
            # log the error
            Logger.exception("Line Collision: ground electric field calculation aborted.")
            return

        system_types = [system.system_type for system in self.tower.systems]

        if "ac" in system_types:
            self.ax.plot(
                self.ef_ground_points,
                self.tower.E_ac_ground,
                label="AC E-Field",
                color="blue",
                linewidth=4,
            )
        if "dc" in system_types or "dc_bipol" in system_types:
            self.ax.plot(
                self.ef_ground_points,
                self.tower.E_dc_ground,
                label="DC E-Field",
                color="red",
                linewidth=4,
            )

        # get the y-axis limits
        if not self.settings.get_ef_auto_axis():
            ymin = self.settings.get_ef_lower_axis()
            ymax = self.settings.get_ef_upper_axis()
            self.ax.set_ylim(ymin, ymax)
        else:
            self.ax.set_ylim(None, None)

        # adjust the legends and labels of the figure
        height = self.settings.get_ef_height_above_ground()
        self._set_ylabel(self.ax, f"Electric Field in kV/m at {height} m over Ground")

        # draw the changes to the plot
        self.fig_canvas.draw_idle()

        # log maximum electric field values
        Logger.info(
            "E-field plot: Height above ground = %s%s",
            str(self.ef_height_above_ground),
            "m",
        )
        Logger.info(
            "E-field plot: Max AC ground E-field = %s %s",
            str(np.max(self.tower.E_ac_ground)),
            "kV/m",
        )
        Logger.info(
            "E-field plot: Max DC ground E-field = %s %s",
            str(np.max(self.tower.E_dc_ground)),
            "kV/m",
        )

    def plot_magnetic_field(self):
        """This method plots the magnetic field on the ground level.

        The magnetic field plot will overlap the tower geometry scatter plot but
        has its value shown on a secondary y-axis. The corresponding legend
        of the magnetic field plot will also be added.
        """
        # clear secondary axis
        self.ax.clear()

        # get the ground points
        start, end, n = self.settings.get_mf_ground_points()
        self.mf_ground_points = np.linspace(start, end, num=n)
        self.mf_height_above_ground = self.settings.get_mf_height_above_ground()
        # calculate the magnetic field
        status = self.tower.calc_magnetic_field(self.mf_ground_points, self.mf_height_above_ground)

        # print text if calculation is unsuccessful due to line collision
        if not status:
            self._msg_line_collision(self.ax)
            # draw changes to the plot
            self.fig_canvas.draw_idle()
            # log the error
            Logger.exception("Line Collision: ground magnetic field calculation aborted.")
            return

        system_types = [system.system_type for system in self.tower.systems]

        if "ac" in system_types:
            self.ax.plot(
                self.mf_ground_points,
                self.tower.B_ac,
                label="AC B-Field",
                color="blue",
                linewidth=4,
            )
        if "dc" in system_types or "dc_bipol" in system_types:
            self.ax.plot(
                self.mf_ground_points,
                self.tower.B_dc,
                label="DC B-Field",
                color="red",
                linewidth=4,
            )

        # get the y-axis limits
        if not self.settings.get_mf_auto_axis():
            ymin = self.settings.get_mf_lower_axis()
            ymax = self.settings.get_mf_upper_axis()
            self.ax.set_ylim(ymin, ymax)
        else:
            self.ax.set_ylim(None, None)

        # adjust the legends and labels of the figure
        height = self.settings.get_mf_height_above_ground()
        self._set_ylabel(self.ax, f"Magnetic Field in \u03BCT at {height} m over Ground")

        # draw changes to the plot
        self.fig_canvas.draw_idle()

        # log maximum magnetic field values
        Logger.info("B-field plot: Height above ground = %sm", str(self.mf_height_above_ground))
        Logger.info(
            "B-field plot: Max AC ground B-field = %s%s",
            str(np.max(self.tower.B_ac)),
            "e-6 T",
        )
        Logger.info(
            "B-field plot: Max DC ground B-field = %s%s",
            str(np.max(self.tower.B_dc)),
            "e-6 T",
        )

    def plot_clear(self):
        """This method clears both axes of the figure."""
        # clear primary axis
        self.ax.clear()
        # clear secondary axis
        self.distance_axis.clear()
        # draw changes to the plot
        self.fig_canvas.draw_idle()

    def set_title(self, title):
        """This method sets the title of the figure."""
        self.fig.suptitle(title, y=0.99)
