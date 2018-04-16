import numpy as np
import scipy as sp
import scipy.interpolate
import matplotlib.pyplot as plt

# Generate some random data
#y = (np.random.random(10) - 0.5).cumsum()
x = np.arange(0.,10.,0.5)


y=[150,
   169.837,
   137.551,
   88.4064,
   60.7195,
   52.6394,
   57.7518,
   75.0752,
   106.073,
   146.347,
   169.53,
   141.713,
   92.1549,
   62.4756,
   53.013,
   57.065,
   73.2293,
   102.921,
   142.739,
   168.795,]

# Interpolate the data using a cubic spline to "new_length" samples
new_length = 50
new_x = np.linspace(x.min(), x.max(), new_length)
new_y = sp.interpolate.interp1d(x, y, kind='cubic')(new_x)

# Plot the results
plt.figure()
plt.subplot(2,1,1)
plt.plot(x, y, '-')
plt.title('Using 1D Cubic Spline Interpolation')

plt.subplot(2,1,2)
plt.plot(new_x, new_y, 'r-')

plt.show()

x=[150,
   169.837,
   137.551,
   88.4064,
   60.7195,
   52.6394,
   57.7518,
   75.0752,
   106.073,
   146.347,
   169.53,
   141.713,
   92.1549,
   62.4756,
   53.013,
   57.065,
   73.2293,
   102.921,
   142.739,
   168.795,]

y=[150,
   205.991,
   274.343,
   291.482,
   254.154,
   203.355,
   161.761,
   136.055,
   129.117,
   147.202,
   199.834,
   269.062,
   292.063,
   258.167,
   207.617,
   165.015,
   137.927,
   129.261,
   144.779,
   194.108,
   ]

h=[0.5,
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
   10,
   ]


plt.plot(h,x, antialiased=True,linestyle = "-",color = "b") #Построение графика
plt.plot(h,y,antialiased=True,linestyle = "-",color = "r")
plt.xlabel(r'$2h$') #Метка по оси x в формате TeX
plt.ylabel(r'$x/y$') #Метка по оси y в формате TeX
plt.grid(True) #Сетка
plt.show() #Показать график

