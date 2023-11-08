# 2. Kuvan oletuskoko 6.4 * 4.8 tuumaa. Haluat tehdä kuvaajan väliltä -3π - 3π.
# Levennä kuva kolminkertaiseksi ja vaihdä käyrien värit sekä piirtotyyli. Lisää myöskin kuvaan selite.


import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-3*np.pi, 3*np.pi, 750, endpoint=True)
C,S = np.cos(X), np.sin(X)

plt.plot(X,C)
plt.plot(X,S)

plt.scatter(X, C, color='green', marker='X')
plt.scatter(X, S, color='red', marker='X')

plt.annotate('Käyrä XS',
             xy=(-10, 0.15), xycoords='data',
             xytext=(0, 0), textcoords='offset points', fontsize=12)
plt.annotate('Käyrä XC',
             xy=(-10, -1), xycoords='data',
             xytext=(0, 0), textcoords='offset points', fontsize=12)

plt.show()