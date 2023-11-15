import tkinter as tk
from tkinter import ttk
from abc import abstractmethod, ABC
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from georunes.petromod.modeler import compute_bulk_dist_coeffs
from georunes.tools.data import get_key


def total_label_color(total):
    if total == 100:
        total_lbl = "100"
        total_lbl_color = "#080"
    else:
        total_lbl = str(total)
        total_lbl_color = "#f00"
    return total_lbl, total_lbl_color


class ViewerTk(ABC):
    def __init__(self, petro_model, part_coeffs, initial_c0, mineral_props=None, suppl_wm_title=None, verbose=0):
        self.verbose = verbose

        # Calculation model
        self.model = petro_model
        self.part_coeffs = part_coeffs
        self.part_coeffs_minerals = self.part_coeffs.keys()
        self.part_coeffs_elements = self.part_coeffs.index.tolist()
        self.initial_c0 = initial_c0
        self.initial_c0_elements = initial_c0.index.tolist()
        if not isinstance(mineral_props, dict):
            list_minerals = self.part_coeffs.iloc[1:, :].keys()
            nb_min = len(list_minerals)
            list_props = np.full(nb_min, round(100 / nb_min, 4))
            mineral_props = dict(zip(list_minerals, list_props))
        self.mineral_props = mineral_props
        new_bulk_dist_coeffs = compute_bulk_dist_coeffs(mineral_props, self.part_coeffs)
        self.model.set_bulk_dist_coeffs(new_bulk_dist_coeffs)
        if self.verbose > 0:
            print("Bulk partition coefficients")
            print(new_bulk_dist_coeffs)

        self.conc_aliases = self.model.get_conc_func_aliases()
        self.missing_minerals = []
        for mineral in self.mineral_props.keys():
            if mineral not in self.part_coeffs_minerals:
                self.missing_minerals.append(mineral)
        self.missing_elements = []
        for element in self.initial_c0_elements:
            if element not in self.part_coeffs_elements:
                self.missing_elements.append(element)

        # Window
        self.fig = Figure(figsize=(6, 4), dpi=100)
        self.ax = self.fig.add_subplot()
        self.root = tk.Tk()
        wm_title = "Fractionation viewer"
        if suppl_wm_title:
            wm_title = "Fractionation viewer - " + suppl_wm_title
        self.root.wm_title("Fractionation viewer" + wm_title)
        self.show_legend = True

        # Concentration choice
        self.active_conc_alias = list(self.conc_aliases.keys())[0]

        # Frame
        self.frame = tk.Toplevel(self.root, )
        self.frame.wm_title("Settings")
        self.frame.grid_columnconfigure(0, weight=1, minsize=100)
        self.frame.grid_columnconfigure(1, weight=2, minsize=200)
        self.frame.minsize(300, 100)  # Minimum width
        self.fill_frame()

        # Canvas
        self.set_canvas()

        # Toolbar
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.root, pack_toolbar=False)
        self.toolbar.update()
        self.toolbar.pack(side=tk.BOTTOM, fill=tk.X)

        # Frame position and settings
        self.root.update()
        dx = self.root.winfo_x() + self.root.winfo_width()
        dy = self.root.winfo_y()
        self.frame.geometry("+%d+%d" % (dx, dy))
        self.frame.protocol("WM_DELETE_WINDOW", self.on_closing_frame)

    def fill_frame(self):
        # Phase selection
        grid_row = 0
        self.combo_conc = ttk.Combobox(self.frame, values=list(self.conc_aliases.values()))
        self.combo_conc.set(self.conc_aliases[self.active_conc_alias])
        self.combo_conc.grid(row=grid_row, columnspan=2, padx=20, pady=20)
        self.combo_conc.bind("<<ComboboxSelected>>", self.update_concentration_func_event)
        grid_row += 1

        # Compositions
        comp_title = tk.Label(self.frame, text="Composition", anchor=tk.CENTER)
        comp_title.grid(row=grid_row, columnspan=2)
        grid_row += 1

        self.label_entry_widgets = []
        total = 0
        for key, value in self.mineral_props.items():
            label = tk.Label(self.frame, text=key)
            entry = tk.Entry(self.frame)
            entry.insert(0, value)
            self.label_entry_widgets.append((label, entry))
            total += value
        # Add other minerals existing in dataset
        for mineral in self.part_coeffs_minerals:
            if mineral not in self.mineral_props.keys():
                label = tk.Label(self.frame, text=mineral)
                entry = tk.Entry(self.frame)
                entry.insert(0, '0')
                self.label_entry_widgets.append((label, entry))

        for label, entry in self.label_entry_widgets:
            label.grid(row=grid_row, column=0, sticky=tk.W, pady=2)
            entry.grid(row=grid_row, column=1, sticky=tk.W, pady=2)
            grid_row += 1

        total = round(total, 4)
        total_label, total_color = total_label_color(total)
        self.label_total = tk.Label(self.frame, text=total_label, fg=total_color)

        self.label_total.grid(row=grid_row + 1, columnspan=2)

        # Set the frame to float
        self.frame.wm_attributes("-topmost", 1)
        update_comp = tk.Button(self.frame, text="Update composition", command=self.update_min_props)
        update_comp.grid(row=grid_row + 2, columnspan=2)
        grid_row += 3

        # Settings
        sep1 = ttk.Separator(self.frame, orient='horizontal')
        sep1.grid(row=grid_row, columnspan=2, sticky="ew", pady=2)
        grid_row += 1

        check_legend = tk.Checkbutton(self.frame, text='Hide/show legend', command=self.toggle_legend)
        check_legend.grid(row=grid_row, columnspan=2)
        grid_row += 1

        # Extra widgets
        self.extra_widgets(grid_row)

    @abstractmethod
    def extra_widgets(self, grid_row):
        pass

    def set_canvas(self):
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def update_bulk_dist_coeffs(self, new_min_props, ):
        new_bulk_dist_coeffs = compute_bulk_dist_coeffs(new_min_props, self.part_coeffs)
        self.model.set_bulk_dist_coeffs(new_bulk_dist_coeffs)
        self.mineral_props = new_min_props
        if self.verbose > 0:
            print("New bulk partition coefficients")
            print(new_bulk_dist_coeffs)
        self.reset_view()

    def update_min_props(self):
        new_min_props = {}
        total = 0
        for label, entry in self.label_entry_widgets:
            new_min_props[label.cget("text")] = float(entry.get())
            total += float(entry.get())

        total_new_label, total_color = total_label_color(total)
        self.label_total.config(text=total_new_label, fg=total_color)
        self.update_bulk_dist_coeffs(new_min_props)

    def update_concentration_func_event(self, _event):
        selected_label = self.combo_conc.get()
        selected_value = get_key(self.conc_aliases, selected_label)
        self.active_conc_alias = selected_value
        self.reset_view()

    @abstractmethod
    def draw(self, element=None):
        pass

    def toggle_legend(self):
        self.show_legend = not self.show_legend
        self.reset_view()

    def loop(self):
        self.root.mainloop()

    def reset_view(self):
        self.fig.clear()
        self.ax = self.fig.add_subplot()
        self.draw()

    def on_closing_frame(self):
        self.canvas.get_tk_widget().destroy()
        self.root.destroy()
