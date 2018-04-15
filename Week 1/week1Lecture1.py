import numpy as np
import matplotlib.pyplot as plt

fixed_cost = 100
per_widget_cost = 5
per_widget_revenue = 10

# Numpy arrays are similar to Python lists. 
widgets = np.arange(41) # starts at 0, goes to the last number before 41
print("\n Here are numbers 0 to 40 representing our x-axis \n")
print(widgets)

def c(x):
    """ The cost function that returns fixed and variable costs """
    cost = per_widget_cost * x + fixed_cost
    return cost
    
def r(x):
    """ The revenue function that returns revenue per widget """
    revenue = per_widget_revenue * x
    return revenue
    
# Send each item in the widget array through the cost function
# This method is called list comprehension, looping through a list in one line
# costs is a list of cost values for each widget
costs = [c(x) for x in widgets] 
print('the costs variable is a list of cost values for each widget')
print(costs)

# Send each item in the widget array through the revenue function
revenues = [r(x) for x in widgets]

# Create a figure and plot our results
plt.figure() # This creates the figure we will work from
plt.plot(widgets, revenues, label="Revenue Line") # Revenue line on the figure
plt.plot(widgets, costs, label="Cost Line") # Cost line on the figure
plt.title("Cost vs Revenue") # Give the figure a title
plt.xlabel("Number of Widgets") # Add a label to the x axis
plt.ylabel("Cost/Revenue") # Add a label to the y axis
plt.legend() # Add a legend to the figure. It pulls in the labels from the lines
plt.show() # This shows the figure we just made.

# Find the breakeven
for widget in widgets:
    # Loop through each value in the widgets array
    if r(widget) >= c(widget):
        # Revenue is >= to cost, so insert the widget number (as a string) into the statement
        print("The break even point is at %s widgets" % widget) 
        break # Now we can leave the loop because we found the point
