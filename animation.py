from matplotlib.animation import FuncAnimation
from plot_hex import create_figure, plot_hex

def get_path_indices(led_pos:dict, keys:list, start_idx:int, end_idx:int) -> list:
    """
    Retorna um caminho com base nas chaves do dicionário e nos indices de inicio e fim

    Parameters
    ----------
    led_pos: dict
        Dicionário com nome do vetor (chave) e vetor (valor)
    keys: list
        Lista com as chaves do dicionário
    start_idx: int
        Índice de inicio
    end_idx: int
        Índice de fim

    Returns
    -------
    list
        Lista contendo as posições com base na lista de chaves e nos indices de inicio e fim

    """

    all_positions = []

    for vertex in led_pos.keys():
        print(vertex)
        if vertex in keys:
            all_positions.extend(led_pos[vertex][start_idx:end_idx + 1])

        print(len(all_positions), "  aaaaa")

   #  positions.append(all_positions[start_idx*2:end_idx*2 + 1])
    # for i in range(1, len(led_pos.keys()) + 1):
    #     if(start_idx < len(all_positions) and end_idx < len(all_positions)):
    #         positions = all_positions[(start_idx-1)*i:(end_idx)*i+1]


    return all_positions


def create_animation(hex_data, led_pos, led_color, start_idx=19, end_idx=37, num_steps=50, interval=150):
    """
    Cria uma animação simples e linear

    hex_data
    """

    path = get_path_indices(led_pos, led_pos.keys(), 19, 37)
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