import numpy as np
import matplotlib.pyplot as plt

# Profit fucntion
def profit(basic_count, advanced_count):
    p = 130 * basic_count + 160 * advanced_count
    return p

# limits
fabrication_limit = 80
finishing_limit = 180

# Range of silver and gold pen production
basic = np.arange(0, 101, 1)  # will act as x axis
advanced = np.arange(0, 101, 1)    # y axis

# Fabrication Limit Line in terms of basic widgets
# fabrication_limit = 1*basic + 2*advanced
b1 = fabrication_limit-2*advanced

# Finishing Limit Line in terms of basic widgets
# finishing_limit = 3*basic + 4*advanced
b2 = (finishing_limit-4*advanced)/3

# Find the intersection of b1 and b2 as a coordinate point for basic and advanced
# fabrication_limit-2*advanced = (finishing_limit-4*advanced)/3
# 80 - 2 * advanced = (180 - 4 * advanced) / 3
# 240 - 6 * advanced = 180 - 4 * advanced
# 60 = 2 * advanced
# 30 = advanced
corner_advanced = 30
# use corner advanced in our b1 line to find corner basic
corner_basic = 80 - 2 * corner_advanced # 20

corner_profit = profit(corner_basic, corner_advanced)  # 7400
# The variables after the % are unpacked in order to populate the print statement
print("With %s basic and %s advanced widgets, there is a profit of %s" % (corner_basic, corner_advanced, corner_profit))

# Corner Profit line in terms of basics
# 7400 = 130 * basic + 160 * advanced
# 130 * basic = 7400 - 160 * advanced
# basic = (7400 - 160 * advanced ) / 130
b0 = (7400 - 160 * advanced) / 130

# Now lets plot our data.
plt.figure()

# Limit the x and y axis
plt.xlim(0, 100)
plt.ylim(0, 100)

# Axis Labels
plt.xlabel('Advanced Widgets')
plt.ylabel('Basic Widgets')
plt.title('Basic and Advanced Widget Production')

# Draw the lines
plt.plot(basic, b1, label='Fabrication Limit', color='r')
plt.plot(basic, b2, label='Finishing Limit', color='g')
plt.plot(basic, b0, 'k--', label='Profit at Corner Point')

# Fill feasible area
plt.fill_between(basic, b1, where=(b1 <= b2), color='b')
plt.fill_between(basic, b2, where=(b2 <= b1), color='b')

plt.legend()
plt.show()

print('The maximum value exists at a corner point: all basic, all advanced, or their intersection' \
      'Profit line based on the intersection falls below the feasible region for all basic')

# Making all basic would be limited by one of the two limitations
basic_fabrication_limit = fabrication_limit/1
basic_finishing_limit = finishing_limit/3
basic_limit = min([basic_fabrication_limit, basic_finishing_limit]) 

# Profit at advanced limit
basic_limit_profit = profit(basic_limit, 0)

print('By producing %s basic widgets and 0 advanced widgets, we have a maximum profit' \
      ' of %s.' % (basic_limit, basic_limit_profit))


##########################################
# Solving the same problem with Pivot Points
##########################################

basic = 130
advanced = 160

# Corner Points
# Identifying them is a manual process
# (basic, advanced)
# corner1 = (0, 0)  zero of both
# corner2 = (0, 40) max out advanced
# corner3 = (60, 0)  max out basic
# corner4 = (20, 30) intersection of inequalities regarding the limits

basic_row =     [0, 0, 60, 20]
advanced_row =  [0, 40, 0, 30]

obj = np.matrix([basic, advanced])
obj = np.transpose(obj)

corners = np.matrix([basic_row, advanced_row])
corners = np.transpose(corners)
results = np.dot(corners, obj)

# Results shows calories burned for each corner point
# Best results are from the (60, 0) option with a profit of $7,800)
print('The total profit for each of the corner points is below')
print(results)
print('Therefore, the maximum profit from the results is %s ' % max(results))
