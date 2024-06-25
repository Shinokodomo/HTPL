import sys
import math
#Для удобства запуска txt файлы находятся в той же директории, что и код
def read_circle_data(filename):
    with open(filename, 'r') as file:
        data = file.readlines()
        x, y = map(float, data[0].strip().split())
        radius = float(data[1].strip())
        return (x, y), radius

def read_points(filename):
    with open(filename, 'r') as file:
        points = []
        for line in file:
            x, y = map(float, line.strip().split())
            points.append((x, y))
        return points

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def point_position_relative_to_circle(point, center, radius):
    px, py = point
    cx, cy = center
    dist = distance(px, py, cx, cy)

    if dist == radius:
        return 0 # точка лежит на окружности
    elif dist < radius:
        return 1 # точка внутри окружности
    else:
        return 2 # точка снаружи окружности

if __name__ == "__main__":
    circle_filename = "circle.txt"
    points_filename = "points.txt"

    center, radius = read_circle_data(circle_filename)
    points = read_points(points_filename)

    results = []
    for point in points:
        position = point_position_relative_to_circle(point, center, radius)
        results.append(position)

    for result in results:
        print(result)
