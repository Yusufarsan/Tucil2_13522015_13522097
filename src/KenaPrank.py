import matplotlib.pyplot as plt

def find_middle(point1, point2):
    new_absis = (point1[0] + point2[0])/2
    new_ordinate = (point1[1] + point2[1])/2
    return new_absis, new_ordinate

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
        bezier_points = bezier_points + create_bezier(array[0], array[1], array[2], num_of_iterations)

    return bezier_points

def algorithm(initial_points, num_of_iterations, index_offset):
    if (num_of_iterations == 1):
        x_values = [point[0] for point in divide(initial_points, num_of_iterations)]
        y_values = [point[1] for point in divide(initial_points, num_of_iterations)]
        plt.plot(x_values, y_values, marker='.', label='Final Graph')

        # Add labels and legend
        plt.title('Multiple Graphs in One Plot')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.legend()
        plt.grid(True)

        plt.subplot(2, 2, 2)
        x_values = [point[0] for point in dnc(initial_points)[0]]
        y_values = [point[1] for point in dnc(initial_points)[0]]
        plt.plot(x_values, y_values, label='Final Graph')
    else:
        x_values = [point[0] for point in dnc(initial_points)[0]]
        y_values = [point[1] for point in dnc(initial_points)[0]]
        plt.plot(x_values, y_values, marker='.', label=f'Iteration #{index_offset}')
        algorithm(dnc(initial_points)[1], num_of_iterations - 1, index_offset + 1)

points = [(-2, 0), (-4, 2), (-2, 4), (2, 4), (4, 2), (2, 0)]
#(-2, 0), (-4, 2), (-2, 4), (2, 4), (4, 2), (2, 0)

# Separate x and y coordinates from the tuples for each graph
x_values1 = [point[0] for point in points]
y_values1 = [point[1] for point in points]

# Plotting both graphs on a single figure
plt.subplot(3, 3, 1)
plt.plot(x_values1, y_values1, marker='.', label='Initial Graph')

algorithm(points, 3, 1)

plt.subplot(2, 2, 2)
plt.plot(x_values1, y_values1, label='Initial Graph')
# Add labels and legend
plt.title('Initial & Final')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)

plt.subplot(2, 2, 3)
plt.plot(x_values1, y_values1, label='Initial Graph')
# Add labels and legend
plt.title('Joined')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)

# Display the combined graph
plt.tight_layout()
plt.show()