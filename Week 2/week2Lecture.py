import numpy as np

###############################
# Inverted Matrix Solution
###############################

#####Example 1#####
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
#[[ 1.2 -1.2]]

#####Example 2#####
#x + 2y = 4
#3x - 5y = 1

eq_1 = [1, 2]
eq_2 = [3, -5]

objective = [4, 1]

var_matrix = np.matrix([eq_1,
                        eq_2])
                        
inv_var_matrix = np.linalg.inv(var_matrix)

results = np.dot(inv_var_matrix, objective)

print(results)
#[[ 2.  1.]]