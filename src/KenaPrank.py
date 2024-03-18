import matplotlib.pyplot as plt

def find_middle(point1, point2):
    new_absis = (point1[0] + point2[0])/2
    new_ordinate = (point1[1] + point2[1])/2
    return new_absis, new_ordinate

def new_set_of_points(points_array):
    new_points = [points_array[0]]
    middle_points = []
    new_array = [points_array[0]]

    for idx in range(len(points_array) - 1):
        middle_points.append(find_middle(points_array[idx], points_array[idx+1]))
        new_array.append(find_middle(points_array[idx], points_array[idx+1]))
    for idx in range(len(middle_points) - 1):
        new_points.append(find_middle(middle_points[idx], middle_points[idx+1]))
        new_array.append(find_middle(middle_points[idx], middle_points[idx+1]))

    new_points.append(points_array[len(points_array) - 1])
    new_array.append(points_array[len(points_array) - 1])

    new_array = sorted(new_array, key=lambda x: x[0])

    return new_points, new_array

def dnc(arr):
    if (len(arr) == 3):
        return new_set_of_points(arr)
    elif (len(arr) == 4):
        left_arr = [arr[0], arr[1], arr[2]]
        right_arr = [arr[1], arr[2], arr[3]]
        left_res = new_set_of_points(left_arr)
        right_res = new_set_of_points(right_arr)

        return left_res[0] + right_res[0], left_res[1] + right_res[1]
    elif (len(arr) == 5):
        left_arr = [arr[0], arr[1], arr[2]]
        right_arr = [arr[2], arr[3], arr[4]]
        left_res = new_set_of_points(left_arr)
        right_res = new_set_of_points(right_arr)
        return left_res[0] + right_res[0], left_res[1] + right_res[1]
    else:
        mid_idx = int(len(arr) / 2)
        left_arr = []
        right_arr = []

        for i in range(mid_idx):
            left_arr.append(arr[i])

        for i in range(mid_idx, len(arr)):
            right_arr.append(arr[i])

        return dnc(left_arr)[0] + dnc(right_arr)[0], dnc(left_arr)[1] + dnc(right_arr)[1]

def algorithm(initial_points, num_of_iterations, index_offset):
    if (num_of_iterations == 1):
        x_values = [point[0] for point in dnc(initial_points)[0]]
        y_values = [point[1] for point in dnc(initial_points)[0]]
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

        draw_arr_x = []
        draw_arr_y = []
        mid_one = x_values[int(len(x_values) * 0.25)], y_values[int(len(x_values) * 0.25)]
        print(mid_one)
        mid_two = x_values[int(len(x_values) * 0.75)], y_values[int(len(x_values) * 0.75)]
        print(mid_two)
        mid = find_middle(mid_one, mid_two)

        for i in range(0, int(len(x_values) * 0.25)):
            draw_arr_x.append(x_values[i])
            draw_arr_y.append(y_values[i])

        draw_arr_x.append(mid[0])
        draw_arr_y.append(mid[1])

        for i in range(int(len(x_values) * 0.75), len(x_values)):
            draw_arr_x.append(x_values[i])
            draw_arr_y.append(y_values[i])

        plt.subplot(2, 2, 3)
        plt.plot(draw_arr_x, draw_arr_y, label='Final Graph')

    else:
        x_values = [point[0] for point in dnc(initial_points)[0]]
        y_values = [point[1] for point in dnc(initial_points)[0]]
        plt.plot(x_values, y_values, marker='.', label=f'Iteration #{index_offset}')
        print(f'panjang x values-{index_offset}: {len(x_values)}')
        algorithm(dnc(initial_points)[1], num_of_iterations - 1, index_offset + 1)

points = [(1, 1), (2, 5), (4, 2), (7, 6), (9, 3), (10, 5)]
#(-2, 0), (-4, 2), (-2, 4), (2, 4), (4, 2), (2, 0)

# Separate x and y coordinates from the tuples for each graph
x_values1 = [point[0] for point in points]
y_values1 = [point[1] for point in points]

# Plotting both graphs on a single figure
plt.subplot(2, 2, 1)
plt.plot(x_values1, y_values1, marker='.', label='Initial Graph')

algorithm(points, 5, 1)

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