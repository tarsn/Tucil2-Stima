import math
import random
import time


def eucl_dist(p1, p2, num_compute):
    n = len(p1)
    return math.sqrt(sum([(p1[i]-p2[i])**2 for i in range(n)])), num_compute + 1


def sort_pair(points, index):
    points = sorted(points, key=lambda x: x[index])
    return points


def brute_force(points, num_compute):
    n = len(points)
    min_distance = math.inf
    closest_pair = None
    for i in range(n):
        for j in range(i+1, n):
            distance, num_compute = eucl_dist(points[i], points[j], num_compute)
            if distance < min_distance:
                min_distance = distance
                closest_pair = (points[i], points[j])
    # print(closest_pair)
    return closest_pair, min_distance, num_compute


def closest_in_strip(min_distance, closest_pair, left_half, right_half, index, num_compute):
    mid = (left_half[-1][index] + right_half[0][index]) / 2

    for p in left_half:
        if (abs(mid - p[index]) < min_distance):
            for q in right_half:
                if (abs(mid - q[index]) < min_distance):
                    qualified = True

                    for i in range(len(p)):
                        if i != index:
                            if abs(q[i] - p[i]) > min_distance:
                                qualified = False

                    if qualified:
                        d, num_compute = eucl_dist(p, q, num_compute)
                        if d < min_distance:
                            min_distance = d
                            closest_pair = (p, q)
    return closest_pair, min_distance, num_compute


def closest_pair_divide_conquer(points, index, num_compute):
    # Basis
    if (len(points) <= 3):
        return brute_force(points, num_compute)


    # Rekurens
    index = (index + 1) % len(points[0])
    min_distance = math.inf
    closest_pair = None

    points = sort_pair(points, index)
    mid = len(points)//2
    left_half = points[:mid]
    right_half = points[mid:]

    pair_left, dist_left, num_compute = closest_pair_divide_conquer(left_half, index, num_compute)
    pair_right, dist_right, num_compute = closest_pair_divide_conquer(right_half, index, num_compute)

    if (dist_left < dist_right):
        min_distance = dist_left
        closest_pair = pair_left
    else:
        min_distance = dist_right
        closest_pair = pair_right

    # print(closest_pair)
    closest_pair, min_distance, num_compute = closest_in_strip(
        min_distance, closest_pair, left_half, right_half, index, num_compute)
    # print(closest_pair)
    return closest_pair, min_distance, num_compute


def printClosestPoint(type, pair, num_compute, distance, time1, time2):
    print("\n"+type)
    print(f"Point 1                     : {pair[0]}\nPoint 2                     : {pair[1]}")
    print(f"Distance                    : {distance}")
    print(f"Number of Eucledian Compute : {num_compute}")
    execution_time =  (time2 - time1)*10**6
    if execution_time > 500:
        execution_time /= 1000 
        print(f"Time Execution              : {(execution_time):.3f} mili seconds")
    else :
        print(f"Time Execution              : {(execution_time):.3f} micro seconds") 




def get_closest_point_n_dimension():
    d = int(input("\nNumber of Dimensions        : "))
    n = int(input("Number of Points            : "))


    points = [tuple(random.uniform(-1000, 1000) for _ in range(d)) for _ in range(n)]

    time1 = time.perf_counter()
    pair1, dist1, num_compute1 = closest_pair_divide_conquer(points, -1, 0)
    time2 = time.perf_counter()
    pair2, dist2, num_compute2 = brute_force(points, 0)
    time3 = time.perf_counter()

    printClosestPoint("Divide and Conquer", pair1, num_compute1, dist1, time1, time2)
    printClosestPoint("Brute Force", pair2, num_compute2, dist2, time2, time3)
    print()
    return points, pair1
