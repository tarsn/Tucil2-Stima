import random
from closest_point_nd import getClosestPoint 
from closest_point_nd import printClosestPoint 
from visualizer_3d import visualize_points

n = int(input("\nNumber of Dimensions        : "))
p = int(input("Number of Points            : "))
points = [tuple(random.uniform(-1000, 1000) for i in range(n)) for i in range(p)]

solution = getClosestPoint(points)
printClosestPoint("Divide and Conquer", solution[0], solution[2], solution[4], solution[6], solution[7])
printClosestPoint("Brute Force", solution[1], solution[3], solution[5], solution[7], solution[8])
print()

if (len(points[0]) == 3):
    inp = int(input("Want to visualized?\n1. Yes\n2. No\n>>> "))
    print()
    if inp == 1 :
      visualize_points(points, solution[0], solution[4])