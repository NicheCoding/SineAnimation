import numpy as np
import matplotlib.pyplot as plt

radius = 1
center = (0,0)

theta = np.linspace(0, 2 * np.pi)

x = center[0] + radius*np.cos(theta)
y = center[1] + radius*np.sin(theta)

fig, ax = plt.subplots() #fig = outline, ax = area, space to draw the thing

ax.spines['bottom'].set_visible(False) #get the bottom spine, move it up to 0 position 
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

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

plt.text(-1.05, 0.5, "π/6", fontsize=12,color = 'red') #30 degree label 
plt.text(-0.9, 0.7, "π/4", fontsize=12,color = 'blue') #45 degree label 
plt.text(-0.7, 0.866, "π/3", fontsize=12,color = 'green') #30 degree label 

#Q3

plt.text(-1.05, -0.6, "π/6", fontsize=12,color = 'red') #30 degree label 
plt.text(-0.9, -0.8, "π/4", fontsize=12,color = 'blue') #45 degree label 
plt.text(-0.7, -0.9, "π/3", fontsize=12,color = 'green') #30 degree label

#Q4 
plt.text(0.9, -0.6, "π/6", fontsize=12,color = 'red') #30 degree label 
plt.text(0.75, -0.8, "π/4", fontsize=12,color = 'blue') #45 degree label 
plt.text(0.55, -0.9, "π/3", fontsize=12,color = 'green') #30 degree label 

#axis 
plt.text(1.04, 0.01, "0", fontsize=12,color = 'black') #0 
plt.text(1.04, -0.1, "2π", fontsize=12,color = 'black') #2 pi
plt.text(-1.1, 0.01, "π", fontsize=12,color = 'black') #pi
plt.text(-0.05, 1.04, "π/2", fontsize=12,color = 'black') #pi/2
plt.text(-0.1, -1.12, "3π/2", fontsize=12,color = 'black') #3pi/2

plt.plot(x,y, color = 'black') #plot x, y
plt.gca().set_aspect('equal') #aspect ratio makes square grid lines
plt.text(-0.28,1.25, "Unit Circle", fontsize = 16)
plt.grid(False)
plt.show()