import numpy as np

a = 2.493
b = 0.911

print(np.degrees(a))
print(np.degrees(b))

c = 137.7
d = 62.3

print(np.radians(c))
print(np.radians(d))

A = np.array([30, 45, 60, 90, 120, 135, 150, 180, 270, 360])

for i in A:
  print(np.radians(i))

print("+=========+")
# tehtävä 2
# kolmion sivujen pituudet a = 1,6m ja b = 2,3m, laske hypotenuusa c

a = 1.6
b = 2.3

c = print(np.hypot(a, b))