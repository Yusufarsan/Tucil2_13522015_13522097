import matplotlib.pyplot as plt
import time


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
    for idx in range(len(middle_points) - 1):
        new_points.append(find_middle(middle_points[idx], middle_points[idx+1]))

    new_points.append(points_array[len(points_array) - 1])

    for idx in range(len(middle_points)):
        new_array.append(middle_points[idx])
        new_array.append(new_points[idx + 1])

    return new_points, new_array


def divideAndConquer(initial_points, num_of_iterations, index_offset):
    # Calculate execute time
    start_time = time.time()

    if num_of_iterations == 1:
        x_values = [point[0] for point in new_set_of_points(initial_points)[0]]
        y_values = [point[1] for point in new_set_of_points(initial_points)[0]]
        plt.plot(x_values, y_values, marker='.', label=f'Final Graph')
        plt.pause(0.5)

        # Add labels and legend
        plt.title('Divide & Conquer')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.legend()
        plt.grid(True)

        # Calculate execution time
        execution_time = (time.time() - start_time) * 1000

        # Display execution time
        plt.text(0.05, 1.05, f'Execution time: {execution_time:.2f} ms', transform=plt.gca().transAxes)

        plt.subplot(2, 2, 2)
        x_values = [point[0] for point in new_set_of_points(initial_points)[0]]
        y_values = [point[1] for point in new_set_of_points(initial_points)[0]]
        plt.plot(x_values, y_values, label='Final Graph')

    else:
        x_values = [point[0] for point in new_set_of_points(initial_points)[0]]
        y_values = [point[1] for point in new_set_of_points(initial_points)[0]]
        print(f'idx-{index_offset}')
        for i in range(len(x_values)):
            print(x_values[i], y_values[i])
        plt.plot(x_values, y_values, marker='.', label=f'Iteration #{index_offset}')
        plt.pause(0.5)

        print(f'initial points-{index_offset}: {new_set_of_points(initial_points)[1]}')
        divideAndConquer(new_set_of_points(initial_points)[1], num_of_iterations - 1, index_offset + 1)
