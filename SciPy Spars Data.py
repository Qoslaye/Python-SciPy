# import numpy as np
# from scipy.sparse import csc_matrix  # You're already using csc_matrix

# dense_matrix = np.array([[1, 0, 0], [0, 0, 2], [3, 0, 4]])
# sparse_matrix = csc_matrix(dense_matrix)  # Use csc_matrix

# print("Dense Matrix:")
# print(dense_matrix)
# print("\nSparse Matrix:")
# print(sparse_matrix)

# # 2 : 
# import numpy as np
# from scipy.sparse import csc_matrix  # You're already using csc_matrix

# arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])
# print(csc_matrix(arr).data)


# # 3 : 
# import numpy as np
# from scipy.sparse import csc_matrix  # You're already using csc_matrix

# arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])

# mat = csc_matrix(arr) 
# mat.eliminate_zeros()

# print(mat)


# # 4 : 
# import numpy as np
# from scipy.sparse import csc_matrix  # You're already using csc_matrix

# arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])

# mat = csc_matrix(arr) 
# mat.sum_duplicates()

# print(mat)



# 5 : 
import numpy as np
from scipy.sparse import csc_matrix

# Create a dense matrix
arr = np.array([[0, 0, 0], [0, 0, 1], [1, 0, 2]])

# Convert the dense matrix to a sparse matrix
sparse_matrix = csc_matrix(arr)

# Since it's already a CSC matrix, you can use it directly or call `tocsc()` if needed
new_array = sparse_matrix.tocsc()  # This is optional since it's already CSC format

print(new_array)

