import math
import random


def eucl_dist(p1, p2):
    n = p1.shape[0]
    return math.sqrt(sum([(p1[i]-p2[i])**2 for i in range(n)]))


def sort_pair(points, index):
    points = sorted(points, key=lambda x: x[index])
    return points


def brute_force(points):
    n = len(points)
    min_distance = math.inf
    closest_pair = None
    for i in range(n):
        for j in range(i+1, n):
            distance = eucl_dist(points[i], points[j])
            if distance < min_distance:
                min_distance = distance
                closest_pair = (points[i], points[j])
    # print(closest_pair)
    return closest_pair, min_distance


def closest_in_strip(min_distance, closest_pair, left_half, right_half, index):
    mid = (left_half[-1][index] + right_half[0][index]) / 2

    for p in left_half:
        if (abs(mid - p[index])):
            for q in right_half:
                if (abs(mid - q[index])):
                    qualified = True

                    for i in range(len(p)):
                        if abs(q[i] - p[i]) > min_distance:
                            qualified = False

                    if qualified :
                        d = eucl_dist(p, q)
                        if d < min_distance:
                            min_distance = d
                            closest_pair = (p, q)

    for p in left_half:
        if abs(p[index] - mid) < min_distance:
            for q in right_half:
                if abs(mid - q[index]) < min_distance and abs(q[1] - p[1]) < min_distance:



                    d = eucl_dist(p, q)
                    if d < min_distance:
                        min_distance = d
                        closest_pair = (p, q)
                        # print(min_distance)
                        # print(closest_pair)
    return closest_pair, min_distance


def closest_pair_divide_conquer(points, index):
    index = (index + 1) % len(points)
    min_distance = math.inf
    closest_pair = None

    # Basis
    if (len(points) <= 3):
        return brute_force(points)

    # Rekurens
    points = sort_pair(points, index)
    mid = len(points)//2
    left_half = points[:mid]
    right_half = points[mid:]


    # print(closest_pair)
    closest_pair, min_distance = closest_in_strip(min_distance, closest_pair, left_half, right_half, index)
    # print(closest_pair)
    return closest_pair, min_distance


points = [(random.uniform(0, 1000), random.uniform(0, 1000)) for _ in range(100000)]

pair1, dist1 = closest_pair_divide_conquer(points)
# pair2, dist2 = brute_force(points)

print(f"pair1 : {pair1}  dist1 : {dist1}")
# print(f"pair2 : {pair2}  dist2 : {dist2}")
