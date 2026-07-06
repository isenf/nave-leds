import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

def config_plot(ax, remove_spines=True, remove_ticks=True):
    """
    Configura a aparência do plot (spines e ticks)

    Parameters
    ---
    ax: 
        eixo do matplotlib
    remove_spines: 
        se True, remove as bordas
    remove_ticks: 
        se True, remove os ticks
    """

    if(remove_ticks):
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xticklabels([])
        ax.set_yticklabels([])

    if(remove_spines):
        for i in ['top', 'right', 'bottom', 'left']:
            ax.spines[i].set_visible(False)

def plot_hex(ax, hex_data, led_positions, led_color, lines_color='.75', lines_tickness=0.5,
             perimeter_color='.75', perimeter_tickness=1, point_size=5, point_edge_tickness=0.5):
    """
    Plota o hexágono e os leds

    Parameters
    ---
    ax: 
        eixo do matplotlib
    hex_data: dict
        dicionário com os dados do hexágono (da função calc_lines_hex)
    led_positions: dict 
        dicionário com a posição dos leds (da função calc_pos_leds)
    lines_color: 
        cor das linhas internas (do centro ao vértice)
    lines_tickness: 
        espessura das linhas internas (do centro ao vértice)
    perimeter_color: 
        cor das linhas externas (entre os vértices)
    perimeter_tickness: 
        espessura das linhas externas (entre os vértices)
    point_size: 
        tamanho dos leds
    point_edge_tickness: 
        espessura da borda dos leds
    """
    hex_x, hex_y = hex_data['perimeter']

    ax.plot(hex_x, hex_y, color=perimeter_color, linewidth=perimeter_tickness)

    for line in hex_data['center_vertices']:
        ax.plot(line[0], line[1], color=lines_color, linewidth=lines_tickness)

    for led_letter, positions in led_positions.items():
        for pos in positions:
            ax.plot(pos[0], pos[1], marker='o', color=led_color[led_letter], 
                    markersize=point_size, markeredgecolor='black', 
                    markeredgewidth=point_edge_tickness)

    ax.set_aspect('equal')

def create_figure(size=(6, 6)):
    """
    Cria uma figura e um eixo

    Parameters
    ---
        size: tupla 
            (largura, altura) da figura
    
    Returns
    ---
        fig, ax: figura e eixo do matplotlib
    """

    fig, ax = plt.subplots(figsize=size)
    config_plot(ax)
    return fig, ax

