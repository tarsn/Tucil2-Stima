import math
import time

def eucl_dist(p1, p2, numCompute):
    n = len(p1)
    return math.sqrt(sum([(p1[i]-p2[i])**2 for i in range(n)])), numCompute + 1

def sortPair(points, idx):
    points = sorted(points, key=lambda x: x[idx])
    return points

def closestPairBF(points, numCompute):
    n = len(points)
    shortestDist = math.inf
    closestPair = None
    for i in range(n):
        for j in range(i+1, n):
            distance, numCompute = eucl_dist(points[i], points[j], numCompute)
            if distance < shortestDist:
                shortestDist = distance
                closestPair = (points[i], points[j])
    return closestPair, shortestDist, numCompute

def closestInStrip(shortestDist, closestPair, leftHalf, rightHalf, idx, numCompute):
    mid = (leftHalf[-1][idx] + rightHalf[0][idx]) / 2

    for p in leftHalf:
        if (abs(mid - p[idx]) < shortestDist):
            for q in rightHalf:
                if (abs(mid - q[idx]) < shortestDist):
                    qualified = True

                    for i in range(len(p)):
                        if i != idx:
                            if abs(q[i] - p[i]) > shortestDist:
                                qualified = False

                    if qualified:
                        d, numCompute = eucl_dist(p, q, numCompute)
                        if d < shortestDist:
                            shortestDist = d
                            closestPair = (p, q)
    return closestPair, shortestDist, numCompute

def closestPairDnC(points, idx, numCompute):
    # Basis
    if (len(points) <= 3):
        return closestPairBF(points, numCompute)

    # Rekurens
    idx = (idx + 1) % len(points[0])
    shortestDist = math.inf
    closestPair = None

    points = sortPair(points, idx)
    mid = len(points)//2
    leftHalf = points[:mid]
    rightHalf = points[mid:]

    pairAtLeft, distAtLeft, numCompute = closestPairDnC(leftHalf, idx, numCompute)
    pairAtRight, distAtRight, numCompute = closestPairDnC(rightHalf, idx, numCompute)

    if (distAtLeft < distAtRight):
        shortestDist = distAtLeft
        closestPair = pairAtLeft
    else:
        shortestDist = distAtRight
        closestPair = pairAtRight

    closestPair, shortestDist, numCompute = closestInStrip(
        shortestDist, closestPair, leftHalf, rightHalf, idx, numCompute)
    return closestPair, shortestDist, numCompute

def printClosestPoint(type, pair, numCompute, distance, time1, time2):
    print("\n"+type)
    print(f"Point 1                     : {pair[0]}")
    print(f"Point 2                     : {pair[1]}")
    print(f"Distance                    : {distance}")
    print(f"Number of Eucledian Compute : {numCompute}")
    executionTime =  (time2 - time1)*10**6
    if executionTime > 500:
        executionTime /= 1000 
        print(f"Time Execution              : {(executionTime):.3f} mili seconds")
    else :
        print(f"Time Execution              : {(executionTime):.3f} micro seconds")

def getClosestPoint(points):
    time1 = time.perf_counter()
    pairDnC, distDnC, numComputeDnC = closestPairDnC(points, -1, 0)
    time2 = time.perf_counter()
    pairBF, distBF, numComputeBF = closestPairBF(points, 0)
    time3 = time.perf_counter()
    return [pairDnC, pairBF, numComputeDnC, numComputeBF, distDnC, distBF, time1, time2, time3]