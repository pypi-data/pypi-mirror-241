from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk
import numpy as np
from georunes.petromod.view.viewertk import ViewerTk


class ConcViewerTk(ViewerTk):
    def __init__(self, petro_model, part_coeffs, initial_c0, mineral_props=None, num_ints=10, verbose=0):
        ViewerTk.__init__(self, petro_model, part_coeffs, initial_c0, mineral_props,
                          suppl_wm_title="Concentration vs liquid fraction", verbose=verbose)
        self.num_ints = num_ints

    def set_canvas(self):
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)

        # Combo box for elements
        self.combo_box = ttk.Combobox(self.root, values=self.initial_c0.index.tolist())
        self.showed_element = self.initial_c0.index.tolist()[0]
        self.combo_box.set(self.showed_element)
        self.combo_box.pack()
        self.combo_box.bind("<<ComboboxSelected>>", self.update_el_event)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def update_el_event(self, _event):
        selected_element = self.combo_box.get()
        self.showed_element = selected_element
        self.reset_view()

    def reset_view(self):
        self.fig.clear()
        self.ax = self.fig.add_subplot()
        self.draw()

    def draw(self, element=None):
        if element and element in self.model.list_elements():
            self.showed_element = element
        self.ax.set_ylabel(self.showed_element)
        self.f = np.linspace(0, 1, self.num_ints + 1)
        concentration_func = self.model.get_concentration_func(self.active_conc_alias)
        self.vals = [concentration_func(self.showed_element, fract, self.initial_c0) for fract in self.f]
        self.line = self.ax.plot(self.f, self.vals)
        self.ax.set_xlabel("F")
        self.canvas.draw()

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
