#Midterm Test
#Summer 2017
#By Benson Lau

import matplotlib.pyplot 
from matplotlib.pyplot import *
import numpy 
from numpy import *

#Question 1
#Using Expedia, the prices for a one-way flight from Chicago to various other 
#cities were recorded. The following table gives the distances from Chicago to
#14 selected cities, along with airfare to each of these cities. 
#Use Python to graph the data and find the least squares line. Then use the 
#equation to determine the marginal cost and predict the cost of a flight to a 
#city that is 1500 miles from Chicago.

#Question 1
import matplotlib.pyplot as plt
import numpy as np
x = [804,1769,1193,1238,2785,1213,895,95,2421,2895,2692,951,2769,2802]
y = [192,184,194,248,315,208,152,293,221,321,291,153,265,339]
best_fit = np.polyfit(x, y, 1)
m=best_fit[0]
b=best_fit[1]
print (('\nThe equation of the least squares line is y = %r x + %r' ) % (m,b))
fig, ax = plt.subplots()
ax.set_title("Prices for Flights to Chicago")
ax.set_xlabel('Distance in miles')
ax.set_ylabel('Price in dollars')
fit_fn = np.poly1d(best_fit)
ax.plot(x,y, 'bo', x, fit_fn(x),'r')
fig.show()
c=round(m*1500+b,2)
print('\nThe marginal cost using the least squares line equation is about 4 cents per mile from Chicago')
print(('\nCost of a flight to a city that is 1500 miles away from Chicago is $%.2f') % round(c,2))

#Question 4
x= arange(0,15,1)
y1= 11 - 2*x
y2= -9 + 2*x
y3= 12 - x
y4= 7 + 0*x
y5= 10.75 + -.75*x
xlim(0,15)
ylim(0,15)
xlabel('x-axis')
ylabel('y-axis')
plot(x,y1, c='b', label='y<=12-2x')
plot(x,y2, c='r', label='y>=-9+2x') 
plot(x,y3, c='g', label='y<=12-x')
plot(x,y4, c='m', label='y<=7')
plot(x,y5, 'k--', label='y=+10.75-.75x')
legend(['y>=12-2*x','y>=-9+2x','y<=12-x','y<=7','y=+10.75-.75x'],loc=1) 

xcorner= [2, 5, 5, 7]
ycorner= [7, 1, 7, 5]
fill(xcorner,ycorner, color='blue', alpha=1)

#fill_between(x,y1,y3, color= 'b')  
#fill_between(x,y2,y4,color='b')
#fill_between(x,y4,y2, where=(y4>=y2), color= 'g') 
#fill_between(x,y2,where=(y2<=y1), color= 'b') 
#fill_between(x,y1,where=(y1<=y2), color= 'b') 
#fill_between(x,y4,where=(y4<7), color= 'b') 
#fill_between(x, y1, y2, color='grey', alpha='0.5')

## to label the points of intersection 
## (https://stackoverflow.com/questions/17576508/python-matplotlib-drawing-linear-inequality-functions)
## plt.plot(x1,f1(x1),'go',markersize=10)
## plt.plot(x2,f1(x2),'go',markersize=10)
## plt.plot(x3,f2(x3),'go',markersize=10)

title ('Shaded Area Shows the Feasible Region') 
show()