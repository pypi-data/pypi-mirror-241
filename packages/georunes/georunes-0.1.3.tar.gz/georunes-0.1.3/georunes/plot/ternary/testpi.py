import georunes.plot.piper.lines
import georunes.plot.piper.plotting
from georunes.plot.piper.piper_axe_subplot import figure

points = [[10,0,0,100,0,0],
          [23.58, 16.15, 8.40+ 1.53, 133+ 0, 12.12, 12.28],
          [32.60, 22, 16+ 12, 139+ 0, 25, 25]
          ]

### Scatter Plot

fig, pax = figure(delta=0.1)
# f2, p2 = ternary.figure(scale=scale)
# pax.set_title("Scatter Plot", fontsize=20)
pax.set_xlim(-0.1, 1.1)
pax.set_ylim(-0.08, 0.94)

pax.set_axis_off()
# Plot a few different styles with a legend

pax.plot(points, marker='D', color='green', label="Green Squares")
pax.set_labels_visible()
pax.gridlines(color="black", num_seps=4, linewidth =0.5)
pax.boundary(linewidth=1.0)
# pax.set_labels_visible()


# tax.legend()
pax.ticks( linewidth=1,  num_ticks= 6, clockwise=True, offset=0.03, fontsize=8)

pax.show()
pax.savefig("D:/Dev/py/graph/test.png")
