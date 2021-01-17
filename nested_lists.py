# Lists can include other lists.

# Creating a Matrix
# Matrices are a structure that has rows and columns.
# To model a matrix in Python,
# we need a new list for each row,
# and we'll need to make sure that each list is the same length
# so that the columns work properly.
# devina has edited twice
# Here's an example matrix not in code:
#
# 1 2 3
# 4 5 6
# To model this matrix in Python:
my_matrix = [[1, 2, 3],
             [4, 5, 6]]
print(my_matrix) # [[1, 2, 3], [4, 5, 6]]

# To determine how many rows are in a multi-dimensional list,
# we need to use the len function on the matrix itself.
# To get the number of columns, we would use len on any row in the matrix
# (assuming that it's a proper matrix with each row having the same number of columns):

row_count = len(my_matrix)
column_count = len(my_matrix[0])
print(row_count) # 2
print(column_count) # 3

# Now if we want to interact with an individual item in the matrix,
# we need to index our variable two times,
# first with the row, and second with the column:

print(my_matrix[0][1]) # 2
