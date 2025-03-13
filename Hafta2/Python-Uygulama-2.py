import math
from itertools import combinations

points = [(1, 2), (4, 6), (7, 8), (2, 1), (5, 3)]
min_distance = float("inf")

def euclideanDistance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

for p1, p2 in combinations(points, 2):
    distance = euclideanDistance(p1, p2)
    min_distance = min(min_distance, distance)

print("Minimum Öklid mesafesi:", min_distance)
