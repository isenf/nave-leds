import matplotlib.pyplot as plt
import numpy as np

angs = [0, 60, 120, 180, 240, 300]
angs_rad = np.deg2rad(angs)

raio = 1
centro_x, centro_y = 0, 0


x = centro_x + raio * np.cos(angs_rad)
y = centro_x + raio * np.sin(angs_rad)

hex_x = np.append(x, x[0])
hex_y = np.append(y, y[0])

fig, ax = plt.subplots(figsize=(6, 6))

leds_lat = 18
leds_diag = 19

A, B, C, D, E, F = [], [], [], [], [], []
arrays = {
    'A': A, 
    'B': B, 
    'C': C, 
    'D': D, 
    'E': E, 
    'F': F
}

for i in range(len(x)):
    arr = list(arrays.items())[i][1]

    for j in range(leds_diag):
        a = j / (leds_diag - 1)
        px = centro_x + a * (x[i] - centro_x)
        py = centro_y + a * (y[i] - centro_y)
        arr.append((px, py))

    for j in range(leds_lat):
        a = (j + 1) / leds_lat
        px = x[i] + a * (x[(i + 1) % len(x)] - x[i])
        py = y[i] + a * (y[(i + 1) % len(y)] - y[i])
        arr.append((px, py))

for k, v in arrays.items():
    v = np.array(v)

ax.set_xticks([])
ax.set_yticks([])
ax.set_xticklabels([])
ax.set_yticklabels([])

for i in ['top', 'right', 'bottom', 'left']:
    ax.spines[i].set_visible(False)

ax.plot(hex_x, hex_y, color='.75', linewidth=2, marker='o', markersize=0)
ax.plot(centro_x, centro_y, marker='o', markersize=0)

for i in range(len(x)):
    ax.plot([centro_x, x[i]], [centro_y, y[i]], color='.75', linewidth=2)


ax.set_aspect('equal')

plt.show()

