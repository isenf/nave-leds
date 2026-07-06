import matplotlib.pyplot as plt
from calc_positions import calc_vertices_hex, calc_lines_hex, calc_pos_leds
from plot_hex import create_figure, plot_hex
from matplotlib.animation import FuncAnimation

RADIUS = 1
CENTER = (0, 0)
LEDS_LAT = 18
LEDS_DIAG = 19

vertices_x, vertices_y = calc_vertices_hex(radius=RADIUS, center=CENTER)

led_pos = calc_pos_leds(vertices_x, vertices_y, center=CENTER,
                        leds_lat=LEDS_LAT, leds_diag=LEDS_DIAG)
led_color = {
    'A': (0x00/255, 0x00/255, 0x00/255, 1.0),  # #02C39A
    'B': (0x00/255, 0x00/255, 0x00/255, 1.0),  # #21A6B0
    'C': (0x00/255, 0x00/255, 0x00/255, 1.0),  # #3F88C5
    'D': (0x00/255, 0x00/255, 0x00/255, 1.0),  # #FF57BB
    'E': (0x00/255, 0x00/255, 0x00/255, 1.0),  # #8D397E
    'F': (0x00/255, 0x00/255, 0x00/255, 1.0),  # #1A1B41
}

hex_data = calc_lines_hex(vertices_x, vertices_y, center=CENTER)

fig, ax = create_figure(size=(6, 6))
# plot_hex(ax, hex_data, led_pos, led_color)

def get_path_indices(led_pos, start_idx, end_idx):
    """

    """

    positions = []
    all_positions = []

    for vertex in led_pos.keys():
        all_positions.extend(led_pos[vertex][start_idx:end_idx + 1])

        print(len(all_positions), "  aaaaa")

    positions = all_positions[start_idx:end_idx + 1]
   #  positions.append(all_positions[start_idx*2:end_idx*2 + 1])
    # for i in range(1, len(led_pos.keys()) + 1):
    #     if(start_idx < len(all_positions) and end_idx < len(all_positions)):
    #         positions = all_positions[(start_idx-1)*i:(end_idx)*i+1]

    print(positions)

    return all_positions


def create_animation(hex_data, led_pos, start_idx=19, end_idx=37, num_steps=50, interval=150):
    """

    """

    path = get_path_indices(led_pos, 19, 37)
    print(len(path))

    fig, ax = create_figure(size=(6,6))
    plot_hex(ax, hex_data, led_pos, led_color)

    point, = ax.plot([], [], 'o', color='red', markersize=5,
                     markeredgecolor='black', markeredgewidth=.5)


    def update(frame):
        i = frame % len(path)
        x, y = path[i]

        point.set_data([x], [y])
        return point,

    anim = FuncAnimation(fig, update,
                         frames=len(path) * 2,
                         interval=interval,
                         blit=True,
                         repeat=True)

    return anim


#plt.show()

if __name__ == '__main__':
    anim = create_animation(hex_data, led_pos)
    plt.show()
