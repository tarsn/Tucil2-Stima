import random
import os.path
from visualizer_3d import *
from closest_point_nd import welcome 
from closest_point_nd import readPoints 
from closest_point_nd import getClosestPoint 
from closest_point_nd import printClosestPoint

welcome()
inp1 = int(input("\nInput Terminal              : 1\nInput file                  : 2\n\033[33m>>> \033[0m"))

n = 0
p = 0
check = True
if inp1 == 1 :
    n = int(input("\nNumber of Dimensions > 0    : "))
    p = int(input("Number of Points > 1        : "))
    points = [tuple(random.uniform(-10000, 10000) for i in range(n)) for i in range(p)]
elif inp1 == 2 :
    path = "test/"
    nameFile = input("\nPut the file in test folder\nInput the file name (ex: test1.txt) : ")
    if os.path.isfile(path+nameFile):
        n, p, check, points = readPoints(path+nameFile)
    else :
        print("\033[31m"+"\nFile doesnt exist. Exiting...\n"+"\033[0m")
        exit()
else :
    print("\033[31m"+"\nInvalid input. Exiting...\n"+"\033[0m")
    exit()

if (n < 1 or p < 2 or check == False):
    print("\033[31m"+"\nInvalid input. Exiting...\n"+"\033[0m")
else :   
    solution = getClosestPoint(points)
    printClosestPoint("Divide and Conquer", solution[0], solution[2], solution[4], solution[6], solution[7])
    printClosestPoint("Brute Force", solution[1], solution[3], solution[5], solution[7], solution[8])
    print()

    if (n == 3):
        inp2 = int(input("Want to visualized?\nYes : 1\nNo  : 0\n\033[33m>>> \033[0m"))
        print()
        if inp2 == 1 :
            visualizePoints3D(points, solution[0], solution[4])
    print("\033[31m"+"Exiting...\n"+"\033[0m")