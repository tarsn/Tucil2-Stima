import matplotlib.pyplot as plt

def visualizePoints3D(points, pair, distance):
    n = len(points)
    x = [points[i][0] for i in range(n)]
    y = [points[j][1] for j in range(n)]
    z = [points[k][2] for k in range(n)]

    fig = plt.figure(figsize=(6,6))
    fig.suptitle('Closest Point', fontsize=16, fontweight='bold')
    ax = plt.axes(projection="3d")
    fg = ax.scatter3D(x, y, z, alpha = 0.4)
    fg = ax.scatter3D(pair[0][0], pair[0][1], pair[0][2], alpha = 1, color='r')
    fg = ax.scatter3D(pair[1][0], pair[1][1], pair[1][2], alpha = 1, color='r')    
    ax.set_title(f"Distance : {(distance):.5f}",loc = "left", fontsize = 9)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_label("Z")
    plt.show()