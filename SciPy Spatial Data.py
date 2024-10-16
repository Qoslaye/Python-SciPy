import numpy as np 
# from scipy.spatial import Delaunay
# import matplotlib.pyplot as plt 

# points = np.array([
#     [2,4], 
#     [4,5],
#     [3,0],
#     [3,2],
#     [4,1]
# ])

# simplices = Delaunay(points).simplices
# plt.triplot(points[:, 0], points[:, 1], simplices)
# plt.scatter(points[:, 0], points[:, 1], color='r')
# plt.show()

 
 #2  ConvexHull  points 


from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt

points = np.array([
    [2, 4],
    [4, 5],
    [3, 0],
    [3, 2],
    [1, 2],
    [5, 0],
    [3, 1],
    [1, 2],
    [0, 2]
])

hull = ConvexHull(points)
hull_points = hull.simplices

plt.scatter(points[:, 0], points[:, 1])

for simple in hull_points:
    plt.plot(points[simple, 0], points[simple, 1], 'k-')

plt.show()
