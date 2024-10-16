# First one 
# import numpy as np
# from scipy.sparse.csgraph import dijkstra
# from scipy.sparse import csr_matrix

# # Define the adjacency matrix
# arr = np.array([
#     [0, 1, 2],
#     [1, 0, 0],
#     [2, 0, 0]
# ])

# # Convert the numpy array to a sparse matrix
# new_array = csr_matrix(arr)

# # Run the Dijkstra algorithm
# distances, predecessors = dijkstra(new_array, return_predecessors=True, indices=0)

# # Print the results
# print("Distances:", distances)
# print("Predecessors:", predecessors)




# Second One
# import numpy as np
# from scipy.sparse.csgraph import bellman_ford
# from scipy.sparse import csr_matrix

# # Define the adjacency matrix
# arr = np.array([
#     [0, -1, 2],
#     [1, 0, 0],
#     [2, 0, 0]
# ])

# new_array = csr_matrix(arr) 
# print(bellman_ford(new_array , return_predecessors=True , indices=0))


# Third one
# import numpy as np
# from scipy.sparse.csgraph import depth_first_order
# from scipy.sparse import csr_matrix

# # Define the adjacency matrix
# arr = np.array([
#     [0, 1,0 ,2],
#     [1, 1, 1 ,1],
#     [2, 1,1,1] , 
#     [0,1,0,1]
# ])

# new_array = csr_matrix(arr) 
# print(depth_first_order(new_array , 1))

# fourth 
import numpy as np
from scipy.sparse.csgraph import breadth_first_order
from scipy.sparse import csr_matrix

# Define the adjacency matrix
arr = np.array([
    [0, 1,0 ,2],
    [1, 1, 1 ,1],
    [2, 1,1,1] , 
    [0,1,0,1]
])

new_array = csr_matrix(arr) 
print(breadth_first_order(new_array , 1))