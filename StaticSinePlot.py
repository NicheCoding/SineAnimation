import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi, 2 * np.pi, 2000)  # 2000 points from -2pi to 2pi
y = np.sin(x) # y = sin(x)

fig, ax = plt.subplots()

ax.plot(x, y, color='blue', label='sin(x)') #draw the curve (in blue) and label sin(x)

ax.set_title("Sine Curve")
ax.set_ylabel("sin(x)")
ax.grid(True)
ax.legend()

ax.set_xlabel("x")

ax.spines['bottom'].set_position('zero') #get the bottom spine, move it up to 0 position 
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
#remove top and right spines so it looks a little better

ax.xaxis.set_label_coords(1.04, 0.52)


ax.xaxis.label.set_verticalalignment('top')

fig.subplots_adjust(bottom=0.25)

plt.show() #show plot
