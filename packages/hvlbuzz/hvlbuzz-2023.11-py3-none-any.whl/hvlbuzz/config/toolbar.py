"""Ui element ConfigToolbar."""

import os

# Import Kivy modules
from kivy.properties import ObjectProperty  # pylint: disable=no-name-in-module
from kivy.uix.boxlayout import BoxLayout

# Import from utility
from ..util.imagebutton import ImageButton
from .. import MODULE_DIR


class ConfigToolbar(BoxLayout):
    """ConfigToolbar contains the following buttons:

    * remove system: remove the curret active system from tower configuration
    * add system: prompts the SystemAddPopup instance
    * refresh plots: redo all calculations and update all plots and tables

    initialization variable(s):

    * tower: Tower instance to be configured
    * data_tabbed_panel: DataTabbedPanel instance containing plots and tables
    * system_add_popup: SystemAddPopup instance for adding new systems
    * config_layout: ConfigLayout instance for system configuration
    * system_selector: SystemSelector dropdown instance for system selection

    The ConfigToolbar layout is contained in the buzz.kv file.
    """

    button_layout = ObjectProperty(None)

    def __init__(
        self, tower, data_tabbed_panel, system_add_popup, config_layout, system_selector, **kwargs
    ):
        super().__init__(**kwargs)

        # Tower instance to be configured
        self.tower = tower
        # DataTabbedPanel instance containing plots and tables
        self.data_tabbed_panel = data_tabbed_panel
        # SystemAddPopup instance for adding new systems
        self.system_add_popup = system_add_popup
        # ConfigLayout instance for system configuration
        self.config_layout = config_layout
        # SystemSelector dropdown instance for system selection
        self.system_selector = system_selector

        # get the path to the images directory
        imagedir = os.path.join(MODULE_DIR, "static", "images")

        # remove system button
        fname = os.path.join(imagedir, "remove.png")
        btn = ImageButton(fname, "Remove selected system from tower")
        btn.bind(on_release=self.remove_system)  # pylint: disable=no-member
        self.button_layout.add_widget(btn)

        # add system button
        fname = os.path.join(imagedir, "add.png")
        btn = ImageButton(fname, "Add system to tower")
        btn.bind(on_release=self.add_system)  # pylint: disable=no-member
        self.button_layout.add_widget(btn)

        # refresh plot button
        fname = os.path.join(imagedir, "line.png")
        btn = ImageButton(fname, "Redraw plots")
        btn.bind(on_release=self.update_plots)  # pylint: disable=no-member
        self.button_layout.add_widget(btn)

    def remove_system(self, event):
        """This method removes the current active system from tower config."""
        if hasattr(self.config_layout, "active_system_idx") and isinstance(
            self.config_layout.active_system_idx, int
        ):
            self.tower.remove_system(self.config_layout.active_system_idx)
            self.config_layout.remove_active_system()
            self.system_selector.setup_system_select()
            self.update_plots(event)

    def add_system(self, _event):
        """This method prompts the SystemAddPopup instance."""
        _add_status = self.system_add_popup.open()

    def update_plots(self, _event):
        """This method prompts the calculation and update of plots."""
        status = self.config_layout.set_params()
        if status:
            self.data_tabbed_panel.update_plots()
