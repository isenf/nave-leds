import matplotlib.pyplot as plt
import numpy as np

angs = [0, 60, 120, 180, 240, 300]
angs_rad = np.deg2rad(angs)

raio = 1
centro_x, centro_y = 0, 0

x = centro_x + raio * np.cos(angs_rad)
y = centro_x + raio * np.sin(angs_rad)

x = np.append(x, x[0])
y = np.append(y, y[0])

fig, ax = plt.subplots(figsize=(6, 6))

ax.set_xticks([])
ax.set_yticks([])
ax.set_xticklabels([])
ax.set_yticklabels([])

for i in ['top', 'right', 'bottom', 'left']:
    ax.spines[i].set_visible(False)
ax.plot(x, y, 'b-', linewidth=2, marker='o', markersize=4)

ax.set_aspect('equal')

plt.show()

