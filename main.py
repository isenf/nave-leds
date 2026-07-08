import matplotlib.pyplot as plt
from calc_positions import calc_vertices_hex, calc_lines_hex, calc_pos_leds
from animation import create_animation, anim_arrow_hor, anim_arrow_ver, anim_arrow_ver2
import asyncio

RADIUS = 1
CENTER = (0, 0)
LEDS_LAT = 18
LEDS_DIAG = 19

vertices_x, vertices_y = calc_vertices_hex(radius=RADIUS, center=CENTER)

led_pos = calc_pos_leds(vertices_x, vertices_y, center=CENTER,
                        leds_lat=LEDS_LAT, leds_diag=LEDS_DIAG)
led_color = {
    'A': (0xFF/255, 0xFF/255, 0xFF/255, 1.0),  # #02C39A
    'B': (0xFF/255, 0xFF/255, 0xFF/255, 0.8),  # #21A6B0
    'C': (0xFF/255, 0xFF/255, 0xFF/255, 0.6),  # #3F88C5
    'D': (0xFF/255, 0xFF/255, 0xFF/255, 0.4),  # #FF57BB
    'E': (0xFF/255, 0xFF/255, 0xFF/255, 0.2),  # #8D397E
    'F': (0xFF/255, 0xFF/255, 0xFF/255, 0.1),  # #1A1B41
}

hex_data = calc_lines_hex(vertices_x, vertices_y, center=CENTER)

# fig, ax = create_figure(size=(6, 6))
# plot_hex(ax, hex_data, led_pos, led_color)

#plt.show()

def teste_arrows():
    anim1 = anim_arrow_hor(hex_data, led_pos, led_color, left=True)
    plt.show(block=False)
    plt.pause(4)
    plt.close()
    
    anim2 = anim_arrow_hor(hex_data, led_pos, led_color, left=False)
    plt.show(block=False)
    plt.pause(4)
    plt.close()

    anim3 = anim_arrow_ver(hex_data, led_pos, led_color, up=True)
    plt.show(block=False)
    plt.pause(6)
    plt.close()

    anim4 = anim_arrow_ver(hex_data, led_pos, led_color, up=False)
    plt.show(block=False)
    plt.pause(6)
    plt.close()

    anim5 = anim_arrow_ver2(hex_data, led_pos, led_color, up=True)
    plt.show(block=False)
    plt.pause(6)
    plt.close()

    anim6 = anim_arrow_ver2(hex_data, led_pos, led_color, up=False)
    plt.show(block=False)
    plt.pause(6)
    plt.close()

if __name__ == '__main__':
    teste_arrows()