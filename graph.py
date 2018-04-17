import numpy as np
import scipy as sp
import scipy.interpolate
import matplotlib.pyplot as plt


x = np.array([0,
              0.5,
              1,
              1.5,
              2,
              2.5,
              3,
              3.5,
              4,
              4.5,
              5,
              5.5,
              6,
              6.5,
              7,
              7.5,
              8,
              8.5,
              9,
              9.5,
              10,])


y=[2, 5.39367, 14.5893, 39.5296, 107.193, 290.611, 782.785, 929.426, 1.74904, 0.0305176, 0.0038758, 0.00164306, 0.00144702, 0.00198556, 0.00356539, 0.00753669, 0.0175884, 0.0435849, 0.112009, 0.294273, 0.783534, ]
y1=[2, 1.23398, 0.783835, 0.538772, 0.45871, 0.697866, 5.09204, 913.557, 1281.35, 778.572, 472.255, 286.44, 173.736, 105.377, 63.9153, 38.7676, 23.5151, 14.2647, 8.6551, 5.25453, 3.195, ]
new_length = 1000
new_x = np.linspace(x.min(), x.max(), new_length)
new_y = sp.interpolate.interp1d(x, y, kind='cubic')(new_x)
new_y1 = sp.interpolate.interp1d(x, y1, kind='cubic')(new_x)





plt.plot(new_x,new_y, antialiased=True,linestyle = "-",color = "b")
plt.plot(new_x,new_y1,antialiased=True,linestyle = "-",color = "r")
plt.xlabel(r'$h$')
plt.ylabel(r'$x/y$')
plt.grid(True)
plt.show()



