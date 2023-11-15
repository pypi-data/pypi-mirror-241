from matplotlib import pyplot as plt

import georunes.plot.piper.lines
import georunes.plot.piper.plotting
from georunes.plot.piper.piper_axe_subplot import figure
from georunes.plot.piper.piper_diag import DiagramPiper

directory = "D:/Dev/py/graph/geoglyph/own/Piper.xlsx"
# source = os.path.join(directory, "WAC_granitoids_pop2.csv")
sheet = 'Sheet2'

piper = DiagramPiper(datasource=directory,
                     #delta=0.1,
                     ticks_number=6, ticks_fontsize=8, ticks_clockwise=True,
                     sheet=sheet, no_legend=True,)

piper.plot()
plt.show()


### Scatter Plot
#
# fig, pax = figure(delta=0.1)
# # f2, p2 = ternary.figure(scale=scale)
# pax.set_title("Scatter Plot", fontsize=20)
# pax.set_xlim(-0.1, 1.1)
# pax.set_ylim(-0.08, 0.94)
# # fig.axis('off')
# # pax.xticks([])
# # pax.yticks([])
# pax.set_axis_off()
# # Plot a few different styles with a legend
#
# pax.plot(points, marker='D', color='green', label="Green Squares")
# pax.set_labels_visible()
# pax.gridlines(color="black", num_seps=4, linewidth =0.5)
# pax.boundary(linewidth=1.0)
# # pax.set_labels_visible()
#
#
# # tax.legend()
# pax.ticks( linewidth=1,  num_ticks= 6, clockwise=True, offset=0.03, fontsize=8)
#
# pax.show()
# pax.savefig("D:/Dev/py/graph/test.png")
