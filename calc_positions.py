import numpy as np

def calc_vertices_hex(radius:float=1.0, center=(0, 0), ang_degrees=None):
    """
    Calcula os vértices de um hexágono regular

    Args:
        radius: raio do hexágono
        center: tupla (x, y) do centro do hexágono
        ang_degrees: lista com os ângulos em graus (padrão: [0, 60, 120, 180, 240, 300])

    Returns:
        x, y: arrays com as coordenadas x e y dos vértices
    """
    
    if(ang_degrees is None):
        ang_degrees = [0, 60, 120, 180, 240, 300]

    ang_rad = np.deg2rad(ang_degrees)
    center_x, center_y = center

    x = center_x + radius * np.cos(ang_rad)
    y = center_y + radius * np.sin(ang_rad)

    return x, y

def calc_pos_leds(vertices_x, vertices_y, center=(0, 0), leds_lat=18, leds_diag=19):
    """
    Calcula a posição dos leds ao longo da lateral e da diagonal

    Parameters
    ---
    vertices_x: 
        posição do vértice no eixo x
    vertices_y: 
        posição do vértice no eixo y
    center: tupla 
        (x, y) do centro do hexágono
    leds_lat: 
        quantidade de leds na lateral
    leds_diag: 
        quantidade de leds na diagonal

    Returns
    ---
    positions: 
        retorna um dicionário contendo uma letra para identificar cada conjunto de led (leds_lat + leds_diag)
    e as posições dos leds nos eixos x e y    
    """

    center_x, center_y = center
    num_vertices = len(vertices_x)

    positions = {chr(65+i): [] for i in range(num_vertices)}

    for i in range(num_vertices):

        for j in range(1, leds_diag + 1):
            # leds na diagonal (do centro ao vértice)
            a = j / (leds_diag + 1)
            px = center_x + a * (vertices_x[i] - center_x)
            py = center_y + a * (vertices_y[i] - center_y)
            positions[chr(65+i)].append([px, py])

        for j in range(1, leds_lat + 1):
            # leds na lateral (entre os vértices)
            a = j / (leds_lat + 1)
            px = vertices_x[i] + a * (vertices_x[(i + 1) % num_vertices] - vertices_x[i])
            py = vertices_y[i] + a * (vertices_y[(i + 1) % num_vertices] - vertices_y[i])
            positions[chr(65+i)].append([px, py])

    for key in positions:
        if(positions[key]):
            positions[key] = np.array(positions[key])

    return positions

def calc_lines_hex(vertices_x, vertices_y, center=(0, 0)):
    """
    Calcula as linhas do hexágono

    Args:
        vertices_x: posição do vértice no eixo x
        vertices_y: posição do vértice no eixo y
        center: tupla (x, y) do centro do hexágono

    Returns:
        retorna um dicionário com coordenadas para plotagem
    """

    center_x, center_y = center
    num_vertices = len(vertices_x)

    hex_x = np.append(vertices_x, vertices_x[0])
    hex_y = np.append(vertices_y, vertices_y[0])

    lines_center = []

    for i in range(num_vertices):
        lines_center.append(([center_x, vertices_x[i]],
                             [center_y, vertices_y[i]]))
        
    return {'perimeter': (hex_x, hex_y), 'center_vertices': lines_center}

