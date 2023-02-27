import random
from closest_point_nd import getClosestPoint 
from closest_point_nd import printClosestPoint 
from visualizer_3d import visualize_points

n = int(input("\nNumber of Dimensions > 0    : "))
p = int(input("Number of Points > 1        : "))

if (n < 1 or p < 2):
   print("Invalid input. Exiting...")
else : 
  points = [tuple(random.uniform(-10000, 10000) for i in range(n)) for i in range(p)]

  solution = getClosestPoint(points)
  printClosestPoint("Divide and Conquer", solution[0], solution[2], solution[4], solution[6], solution[7])
  printClosestPoint("Brute Force", solution[1], solution[3], solution[5], solution[7], solution[8])
  print()

  if (len(points[0]) == 3):
      inp = int(input("Want to visualized?\nYes : 1\nNo  : 0\n>>> "))
      print()
      if inp == 1 :
        visualize_points(points, solution[0], solution[4])