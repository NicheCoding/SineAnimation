import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation 
from matplotlib.animation import FuncAnimation 

frames=300
interval=50

#Sine Function (Left)
x_v = np.linspace(0, 2 * np.pi, 300) #sets up 300 points for sinx (going to be same for circle) x_v = for sine 



fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
fig.suptitle("Synced Sine Wave and Circular Motion", fontsize=25)

ax1.set_title("Sine Function", fontsize=20)
ax1.set_xlim(0, 2 * np.pi)
ax1.set_ylim(-1.2, 1.2)

ax1.spines['bottom'].set_position('zero') #get the bottom spine, move it up to 0 position 
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

xticks = [0, np.pi/2, np.pi, 3 * np.pi /2, 2*np.pi]
ax1.set_xticks(xticks)

xtick_labels = ['0','π/2','π','3π/2', '2π']
ax1.set_xticklabels(xtick_labels)

dot_sine, = ax1.plot([],[],'o', color = 'purple')


ax1.plot(x_v, np.sin(x_v), color='black')


#Circle Function (Right)
radius = 1
center = (0,0)
ax2.set_xlim(-1.5, 1.5)
ax2.set_ylim(-1.5, 1.5)
ax2.set_aspect('equal')
ax2.set_title("Unit Circle", fontsize =20,pad=40)
ax2.grid(True)



theta = np.linspace(0, 2 * np.pi, 300) #300 values of theta
ax2.plot(radius * np.cos(theta), radius * np.sin(theta), color='black')
dot_circle, = ax2.plot([], [], 'o', color='purple')

ax2.spines['bottom'].set_visible(False) #removing all spines 
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['left'].set_visible(False)

plt.xticks([])  # remove x-axis labels
plt.yticks([])  # remove y-axis labels

theta_deg1 = 30
theta_rad1 = np.radians(theta_deg1)
t = np.linspace(-radius, radius, 100)

linex1 = center[0] + t * np.cos(theta_rad1)
liney1 = center[1] + t * np.sin(theta_rad1)

plt.plot(linex1, liney1, color='red')
plt.plot(-linex1, liney1, color='red')



theta_deg2 = 45
theta_rad2 = np.radians(theta_deg2)
t = np.linspace(-radius, radius, 100)

linex2 = center[0] + t * np.cos(theta_rad2)
liney2 = center[1] + t * np.sin(theta_rad2)

plt.plot(linex2, liney2, color='blue')
plt.plot(-linex2, liney2, color='blue')


theta_deg3 = 60
theta_rad3 = np.radians(theta_deg3)
t = np.linspace(-radius, radius, 100)

linex3 = center[0] + t * np.cos(theta_rad3)
liney3 = center[1] + t * np.sin(theta_rad3)

plt.plot(linex3, liney3, color='green')
plt.plot(-linex3, liney3, color='green')

theta_rad4 = np.radians(90)
t = np.linspace(-radius, radius, 100)
linex4 = center[0] + t * np.cos(theta_rad4)
liney4 = center[1] + t * np.sin(theta_rad4)


plt.plot(linex4, liney4, color='black', linewidth = 2)

theta_rad5 = np.radians(180)
t = np.linspace(-radius, radius, 100)
linex5 = center[0] + t * np.cos(theta_rad5)
liney5 = center[1] + t * np.sin(theta_rad5)

plt.plot(linex5, liney5, color='black', linewidth = 2)

#Q1 
plt.text(0.9, 0.5, "π/6", fontsize=12,color = 'red') #30 degree label 
plt.text(0.75, 0.7, "π/4", fontsize=12,color = 'blue') #45 degree label 
plt.text(0.55, 0.866, "π/3", fontsize=12,color = 'green') #30 degree label 

#Q2

plt.text(-1.02, 0.5, "5π/6", fontsize=12,color = 'red') #30 degree label 
plt.text(-0.87, 0.7, "3π/4", fontsize=12,color = 'blue') #45 degree label 
plt.text(-0.67, 0.866, "2π/3", fontsize=12,color = 'green') #30 degree label 

#Q3

plt.text(-1.02, -0.6, "7π/6", fontsize=12,color = 'red') #30 degree label 
plt.text(-0.87, -0.8, "5π/4", fontsize=12,color = 'blue') #45 degree label 
plt.text(-0.67, -1, "4π/3", fontsize=12,color = 'green') #30 degree label

#Q4 
plt.text(0.87, -0.6, "11π/6", fontsize=12,color = 'red') #30 degree label 
plt.text(0.70, -0.8, "7π/4", fontsize=12,color = 'blue') #45 degree label 
plt.text(0.5, -1, "5π/3", fontsize=12,color = 'green') #30 degree label 

#axis 
plt.text(1.04, 0.01, "0", fontsize=12,color = 'black') #0 
plt.text(1.04, -0.1, "2π", fontsize=12,color = 'black') #2 pi
plt.text(-1.1, 0.01, "π", fontsize=12,color = 'black') #pi
plt.text(-0.05, 1.04, "π/2", fontsize=12,color = 'black') #pi/2
plt.text(-0.1, -1.12, "3π/2", fontsize=12,color = 'black') #3pi/2


coord_label = ax2.text(1, 1, "", fontsize=12, color='black')

# Animation function
def update(frame):
    # Sine wave dot
    x = x_v[frame]
    y = np.sin(x)
    dot_sine.set_data([x], [y])

    # Circle dot (same angle)
    angle = 2 * np.pi * frame / frames
    x_circ = radius * np.cos(angle)
    y_circ = radius * np.sin(angle)
    dot_circle.set_data([x_circ], [y_circ])

    dot_sine.set_data([x], [y])  # Must be sequences
    coord_label.set_text(f"sin(θ) = {y_circ:.2f}") #set y-coords (as sine because duh) round 2 dec places

    return dot_sine, dot_circle, coord_label


# Create animation
ani = FuncAnimation(fig, update, frames=frames, interval=interval, blit=True)


plt.show()
