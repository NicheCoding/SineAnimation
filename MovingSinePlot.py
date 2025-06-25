import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation 

x = np.linspace(0, 2 * np.pi, 300) #sets up 300 points for sinx (going to be same for circle)
y = np.sin(x) #the y values are literally calculating sine 

fig, ax = plt.subplots() #fig = outline, ax = area, space to draw the thing
ax.plot(x, y, color='black', label='Moving Sine Plot') #draw the curve (in black) and label sin(x)

ax.spines['bottom'].set_position('zero') #get the bottom spine, move it up to 0 position 
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

xticks = [0, np.pi/2, np.pi, 3 * np.pi /2, 2*np.pi]
ax.set_xticks(xticks)

xtick_labels = ['0','π/2','π','3π/2', '2π']
ax.set_xticklabels(xtick_labels)

dot, = ax.plot([],[],'o', color = 'purple') #purple dot ('o' = filled circle) with no position ([], [] = not visible)

ax.set_xlim(0, 2 * np.pi) #x-axis is 0 to 2 pi 
ax.set_ylim(-1.1, 1.1) #y axis is -1 to 1 

def init(): #initialize dot to start at no position 
    dot.set_data([],[])
    return dot,

def update(frame): #update where dot is every frame 
    dot.set_data([x[frame]], [y[frame]]) #use sine wave coords to move dot frame by frame 
    return dot,

ani = animation.FuncAnimation(
    fig, update, frames=len(x), init_func=init,
    interval=50 , blit=True
)
#interval = time between frames, blit = True means only redraw parts that change (more efficient)

plt.show() #really important so it shows up 