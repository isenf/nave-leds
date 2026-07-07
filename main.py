import matplotlib.pyplot as plt
from calc_positions import calc_vertices_hex, calc_lines_hex, calc_pos_leds
from animation import create_animation

RADIUS = 1
CENTER = (0, 0)
LEDS_LAT = 18
LEDS_DIAG = 19

vertices_x, vertices_y = calc_vertices_hex(radius=RADIUS, center=CENTER)

led_pos = calc_pos_leds(vertices_x, vertices_y, center=CENTER,
                        leds_lat=LEDS_LAT, leds_diag=LEDS_DIAG)
led_color = {
    'A': (0x00/255, 0x00/255, 0x00/255, 0.2),  # #02C39A
    'B': (0x00/255, 0x00/255, 0x00/255, 0.2),  # #21A6B0
    'C': (0x00/255, 0x00/255, 0x00/255, 0.2),  # #3F88C5
    'D': (0x00/255, 0x00/255, 0x00/255, 0.2),  # #FF57BB
    'E': (0x00/255, 0x00/255, 0x00/255, 0.2),  # #8D397E
    'F': (0x00/255, 0x00/255, 0x00/255, 0.2),  # #1A1B41
}

hex_data = calc_lines_hex(vertices_x, vertices_y, center=CENTER)

# fig, ax = create_figure(size=(6, 6))
# plot_hex(ax, hex_data, led_pos, led_color)

#plt.show()

if __name__ == '__main__':
    anim = create_animation(hex_data, led_pos, led_color)
    plt.show()
