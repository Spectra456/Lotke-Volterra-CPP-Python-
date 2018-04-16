import numpy as np
import scipy as sp
import scipy.interpolate
import matplotlib.pyplot as plt

# Generate some random data
#y = (np.random.random(10) - 0.5).cumsum()
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


y=[300,
   224.652,
   65.1657,
   24.2603,
   16.5596,
   18.0452,
   26.7053,
   47.5693,
   93.1977,
   183.485,
   300.012,
   224.619,
   65.1525,
   24.2576,
   16.5592,
   18.046,
   26.7074,
   47.5741,
   93.208,
   183.504,
   300.024,]
y1=[150,
    384.889,
    453.359,
    334.862,
    223.63,
    147.491,
    99.6913,
    72.2949,
    61.4659,
    72.8194,
    150.024,
    384.927,
    453.347,
    334.842,
    223.615,
    147.482,
    99.6855,
    72.2919,
    61.4656,
    72.8242,
    150.048,
    ]
# Interpolate the data using a cubic spline to "new_length" samples
new_length = 1000
new_x = np.linspace(x.min(), x.max(), new_length)
new_y = sp.interpolate.interp1d(x, y, kind='cubic')(new_x)
new_y1 = sp.interpolate.interp1d(x, y1, kind='cubic')(new_x)





plt.plot(new_x,new_y, antialiased=True,linestyle = "-",color = "b") #Построение графика
plt.plot(new_x,new_y1,antialiased=True,linestyle = "-",color = "r")
plt.xlabel(r'$h$') #Метка по оси x в формате TeX
plt.ylabel(r'$x/y$') #Метка по оси y в формате TeX
plt.grid(True) #Сетка
plt.show() #Показать



