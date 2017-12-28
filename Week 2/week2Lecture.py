import numpy as np

###############################
# Inverted Matrix Solution
###############################

#2x - 3y = 6
#x + y = 0

# The equations with each row having an x value and then a y value
eq_1 = [2, -3]
eq_2 = [1, 1]

objective = [6, 0]

var_matrix = np.matrix([eq_1,
                        eq_2])

# Inverse the matrix
inv_var_matrix = np.linalg.inv(var_matrix)

# Multiply the inverse matrix with our objective
results = np.dot(inv_var_matrix, objective)

# Results are the value for x and y that meets the objective 
print(results)
#[[1.2,-1.2]]