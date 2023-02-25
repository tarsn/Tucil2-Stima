import matplotlib.pyplot as plt
import random

# points = [list(random.uniform(-1000, 1000) for _ in range(3)) for _ in range(10)]

points = [[1,2,3], [4,5,6], [7,8,9]]



def visualize_points(points, pair):
    n = len(points)
    x = [points[i][0] for i in range(n)]
    y = [points[j][1] for j in range(n)]
    z = [points[k][2] for k in range(n)]

    plt.figure(figsize=(6,6))
    ax = plt.axes(projection="3d")
    fg = ax.scatter3D(x, y, z, alpha = 0.4)
    fg = ax.scatter3D(pair[0][0], pair[0][1], pair[0][2], alpha = 1, color='r')
    fg = ax.scatter3D(pair[1][0], pair[1][1], pair[1][2], alpha = 1, color='r')    
    ax.set_title("Closest Points")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_label("Z")
    plt.show()
# print(x)