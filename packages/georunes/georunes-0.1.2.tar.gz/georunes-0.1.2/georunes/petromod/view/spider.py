import tkinter as tk
from tkinter import ttk
from georunes.petromod.view.viewertk import ViewerTk
from georunes.tools.reservoirs import get_reservoir_norm


class SpiderViewerTk(ViewerTk):
    def __init__(self, petro_model, part_coeffs, initial_c0, fract_values, mineral_props=None, verbose=0, norm="CI"):
        ViewerTk.__init__(self, petro_model, part_coeffs, initial_c0, mineral_props,
                          suppl_wm_title="Spider diagram by fractionation degree", verbose=verbose)
        self.norm = get_reservoir_norm(norm)
        self.fract_values = fract_values
        self.line = None

    def extra_widgets(self, grid_row):
        if len(self.missing_minerals) > 0:
            sep2 = ttk.Separator(self.frame, orient='horizontal')
            sep2.grid(row=grid_row, columnspan=2, sticky="ew", pady=2)
            grid_row += 1
            label_content = "Minerals missing in the dataset: " + str(self.missing_minerals)
            label_warning = tk.Label(self.frame, text=label_content, fg="#f00")
            label_warning.grid(row=grid_row, columnspan=2)

        if len(self.missing_elements) > 0:
            grid_row += 1
            label_content2 = "Elements missing in the dataset: " + str(self.missing_elements)
            label_warning2 = tk.Label(self.frame, text=label_content2, fg="#f00")
            label_warning2.grid(row=grid_row, columnspan=2)

    def draw(self, element=None):
        list_elements = self.model.list_elements()
        concentration_func = self.model.get_concentration_func(self.active_conc_alias)
        for f in self.fract_values:

            values = [concentration_func(el, f, self.initial_c0) / self.norm[el] for el in list_elements]
            self.line = self.ax.semilogy(list_elements, values, label='F={}'.format(f))
        if self.show_legend:
            self.ax.legend()
        self.canvas.draw()
