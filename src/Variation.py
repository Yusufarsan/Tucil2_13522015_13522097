import matplotlib.pyplot as plt
import time


def find_middle(point1, point2):
    new_absis = (point1[0] + point2[0])/2
    new_ordinate = (point1[1] + point2[1])/2
    return new_absis, new_ordinate


def calculate_distance(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5


def find_nearest_pair(points1, points2):
    min_distance = float('inf')
    nearest_pair = None

    for point1 in points1:
        for point2 in points2:
            distance = calculate_distance(point1, point2)
            if distance < min_distance:
                min_distance = distance
                nearest_pair = (point1, point2)

    return nearest_pair

def orientation(p, q, r):
    # Function to find orientation of triplet (p, q, r).
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # Collinear
    return 1 if val > 0 else 2  # Clockwise or counterclockwise

def on_segment(p, q, r):
    # Function to check if point q lies on segment pr.
    return (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and
            q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1]))

def isIntersect(points1, points2):
    # Function to check if two graphs intersect based on arrays of points.
    for i in range(len(points1) - 1):
        for j in range(len(points2) - 1):
            p1, q1 = points1[i], points1[i + 1]
            p2, q2 = points2[j], points2[j + 1]
            o1 = orientation(p1, q1, p2)
            o2 = orientation(p1, q1, q2)
            o3 = orientation(p2, q2, p1)
            o4 = orientation(p2, q2, q1)

            # General case
            if o1 != o2 and o3 != o4:
                return True

            # Special Cases: collinear segments
            if o1 == 0 and on_segment(p1, p2, q1):
                return True
            if o2 == 0 and on_segment(p1, q2, q1):
                return True
            if o3 == 0 and on_segment(p2, p1, q2):
                return True
            if o4 == 0 and on_segment(p2, q1, q2):
                return True

    return False


def create_bezier(ctrl1, ctrl2, ctrl3, iterations):
    bezier_points = []
    bezier_points.append(ctrl1)  # add the first control point
    populate_bezier_points(ctrl1, ctrl2, ctrl3, 0, iterations, bezier_points)
    bezier_points.append(ctrl3)  # add the last control point
    return bezier_points


def populate_bezier_points(ctrl1, ctrl2, ctrl3, current_iteration, iterations, bezier_points):
    if current_iteration < iterations:
        # calculate next mid points
        mid_point1 = find_middle(ctrl1, ctrl2)
        mid_point2 = find_middle(ctrl2, ctrl3)
        mid_point3 = find_middle(mid_point1, mid_point2)  # the next control point
        current_iteration += 1
        populate_bezier_points(ctrl1, mid_point1, mid_point3, current_iteration, iterations, bezier_points)  # left branch
        bezier_points.append(mid_point3)  # add the next control point
        populate_bezier_points(mid_point3, mid_point2, ctrl3, current_iteration, iterations, bezier_points)  # right branch


def create_3_tuples(points):
    n = len(points)
    three_tuples = []

    for i in range(n - 2):
        three_tuples.append([points[i], points[i + 1], points[i + 2]])

    return three_tuples


def divide(initial_points, num_of_iterations):
    sub_arrays = create_3_tuples(initial_points)
    bezier_points = []
    for array in sub_arrays:
        bezier_points.append(create_bezier(array[0], array[1], array[2], num_of_iterations))

    return bezier_points

def dnc_variation(points, iterations):
    # Calculate execute time
    start_time = time.time()

    # Separate x and y coordinates from the tuples for each graph
    x_values1 = [point[0] for point in points]
    y_values1 = [point[1] for point in points]

    # Plotting both graphs on a single figure
    plt.subplot(2, 3, 4)
    plt.plot(x_values1, y_values1, marker='.', label='Initial Graph')

    arrays = divide(points, iterations)
    for array in arrays:
        x_values = [point[0] for point in array]
        y_values = [point[1] for point in array]
        plt.plot(x_values, y_values, marker='.', label='Final Graph')

    # Add labels and legend
    plt.title('Divided Bezier')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)

    plt.subplot(2, 3, 5)
    x_values = []
    y_values = []
    temp_idx = 0

    for idx in range(len(arrays) - 1):
        nearest_pair = find_nearest_pair(arrays[idx], arrays[idx+1])

        # Get the index of nearest points
        element_to_find = nearest_pair[0]
        index1 = arrays[idx].index(element_to_find)

        element_to_find = nearest_pair[1]
        index2 = arrays[idx + 1].index(element_to_find)

        if isIntersect(arrays[idx], arrays[idx+1]):
            for i in range(temp_idx, index1 + 1):
                x_values.append(arrays[idx][i][0])
                y_values.append(arrays[idx][i][1])
        else:
            for i in range(temp_idx, int(len(arrays[idx])/2) + 1):
                x_values.append(arrays[idx][i][0])
                y_values.append(arrays[idx][i][1])

        temp_idx = index2 + 1

    if isIntersect(arrays[-2], arrays[-1]):
        for i in range(temp_idx, len(arrays[len(arrays) - 1])):
            x_values.append(arrays[len(arrays) - 1][i][0])
            y_values.append(arrays[len(arrays) - 1][i][1])
    else:
        for i in range(int(len(arrays[-1])/2), len(arrays[-1])):
            x_values.append(arrays[len(arrays) - 1][i][0])
            y_values.append(arrays[len(arrays) - 1][i][1])

    plt.plot(x_values1, y_values1, label='Initial Graph')
    plt.plot(x_values, y_values, label='Final Graph')

    # Calculate execution time
    execution_time = (time.time() - start_time) * 1000

    # Add labels and legend
    plt.title('Pure D&C Variation')
    plt.xlabel(f'Execution time: {execution_time:.2f} ms')
    plt.ylabel('Y')
    plt.grid(True)
