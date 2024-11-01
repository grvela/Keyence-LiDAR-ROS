import random

class FakeLaser:

    def __init__(self):
        pass

    def get_laser_scan(self):
        points = []
        min_distance = 4200
        max_distance = 5000
        num_points = 751
        points = random.sample(range(min_distance, max_distance), num_points)

        points_f = []
        for i in range(len(points)):
            points_f.append(float(points[i] / 1000.0))
        return points_f

if __name__ == '__main__':
    app = FakeLaser()
    data = app.tick()
    print(data)