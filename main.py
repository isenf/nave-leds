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
led_color = {
    'A': (0x02/255, 0xC3/255, 0x9A/255, 1.0),  # #02C39A
    'B': (0x21/255, 0xA6/255, 0xB0/255, 1.0),  # #21A6B0
    'C': (0x3F/255, 0x88/255, 0xC5/255, 1.0),  # #3F88C5
    'D': (0xFF/255, 0x57/255, 0xBB/255, 1.0),  # #FF57BB
    'E': (0x8D/255, 0x39/255, 0x7E/255, 1.0),  # #8D397E
    'F': (0x1A/255, 0x1B/255, 0x41/255, 1.0),  # #1A1B41
}

hex_data = calc_lines_hex(vertices_x, vertices_y, center=CENTER)

fig, ax = create_figure(size=(6, 6))
plot_hex(ax, hex_data, led_pos, led_color)

plt.show()

