import matplotlib.pyplot as plt
from calc_positions import calc_vertices_hex, calc_lines_hex, calc_pos_leds
from plot_hex import create_figure, plot_hex

RADIUS = 1
CENTER = (0, 0)
LEDS_LAT = 18
LEDS_DIAG = 19

vertices_x, vertices_y = calc_vertices_hex(radius=RADIUS, center=CENTER)

led_pos = calc_pos_leds(vertices_x, vertices_y, center=CENTER, 
                        leds_lat=LEDS_LAT, leds_diag=LEDS_DIAG)

hex_data = calc_lines_hex(vertices_x, vertices_y, center=CENTER)

fig, ax = create_figure(size=(6, 6))
plot_hex(ax, hex_data, led_pos)

plt.show()

