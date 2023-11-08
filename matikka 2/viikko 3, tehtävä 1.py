# 1. Aiemmassa tehtävässä piti tehdä taulukko näistä radiaaneina.
# Merkkaile nyt nämä yksikköympyrälle esimerkin mukaan: 30, 45, 60, 90, 120, 150, 180, 270.


from matplotlib import pyplot as plt, patches
import numpy as np
from fractions import Fraction as fr

import matplotlib as mpl

fig = plt.figure()
ax = fig.subplots()

ymp = patches.Circle((0, 0), radius=1, fill=0)
ax.add_patch(ymp)

# Move left y-axis and bottom x-axis to centre, passing through (0,0)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Show ticks in the left and lower axes only
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

ax.axis('equal')

plt.xticks([-1, 0, 1], minor=True)
plt.yticks([-1, 0, 1])

pist_xy=np.array([np.pi/6, np.pi/4, np.pi/3, np.pi/2, np.pi/1.5, np.pi/1.2, np.pi, np.pi/0.666])


varit=np.array(['red', 'green', 'blue', 'pink', 'yellow', 'black', 'orange', 'purple'])

x = np.cos(pist_xy)
y = np.sin(pist_xy)


plt.scatter(x, y, color=varit, marker='X')

plt.annotate(r'$(\frac{\pi}{6})$',
             xy=(np.cos(np.pi/6), np.sin(np.pi/6)), xycoords='data',
             xytext=(+10, +0), textcoords='offset points', fontsize=12)
plt.annotate(r'$(\frac{\pi}{4})$',
             xy=(np.cos(np.pi/4), np.sin(np.pi/4)), xycoords='data',
             xytext=(+10, +0), textcoords='offset points', fontsize=12)
plt.annotate(r'$(\frac{\pi}{3})$',
             xy=(np.cos(np.pi/3), np.sin(np.pi/3)), xycoords='data',
             xytext=(+10, +0), textcoords='offset points', fontsize=12)
plt.annotate(r'$(\frac{\pi}{2})$',
             xy=(np.cos(np.pi/2), np.sin(np.pi/2)), xycoords='data',
             xytext=(+5, +5), textcoords='offset points', fontsize=12)
plt.annotate(r'$(\frac{\pi}{1.5})$',
             xy=(np.cos(np.pi/1.5), np.sin(np.pi/1.5)), xycoords='data',
             xytext=(-20, +10), textcoords='offset points', fontsize=12)
plt.annotate(r'$(\frac{\pi}{1.2})$',
             xy=(np.cos(np.pi/1.2), np.sin(np.pi/1.2)), xycoords='data',
             xytext=(-20, +10), textcoords='offset points', fontsize=12)
plt.annotate(r'$({\pi})$',
             xy=(np.cos(np.pi), np.sin(np.pi)), xycoords='data',
             xytext=(-20, +10), textcoords='offset points', fontsize=12)
plt.annotate(r'$(\frac{\pi}{0.666})$',
             xy=(np.cos(np.pi/0.666), np.sin(np.pi/0.666)), xycoords='data',
             xytext=(-20, -20), textcoords='offset points', fontsize=12)


plt.show()


