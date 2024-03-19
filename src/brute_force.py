# ini file untuk nge handle pemrosesan data dan berbagai pengolahan lainnya

import matplotlib.pyplot as plt
import numpy as np
import time

def generate_pascal(n):
    '''Generate the n-th pascal pattern'''
    pascal = []
    for i in range(n):  # Change to n+1 to include the n-th row
        row = [1 if j == 0 or j == i else pascal[i-1][j-1] + pascal[i-1][j] for j in range(i+1)]
        pascal.append(row)
    return pascal[-1]  # Return the last row
# Test the function
# n = 3
# print(generate_pascal(n))

def bezier(t, control_points):
    '''Get the point from the bezier function with the given t'''
    # Initialize the pascal pattern by using generate_pascal function with n = len(control_points)
    pascal = generate_pascal(len(control_points))

    if len(pascal) != len(control_points):
        print("Error: number of pascal pattern is not equal to number of control points")
        return None

    # Calculate the point with the given t
    result_point = np.zeros(2)
    for n in range (len(control_points)):
        result_point += pascal[n] * ( (1 - t)**(len(control_points) - 1 - n) ) * (t**n) * ( np.array(control_points[n]) )

    return tuple(result_point)

def brute_force_process (control_points, iterate_number):
    '''Process the brute force method (visualize the bezier curve with the given control points and iterate number)'''
    # Calculate execute time
    start_time = time.time()

    # Generate array t from 0 to 1 in iterate_number steps
    t = np.linspace(0, 1, iterate_number)

    # Generate points from bezier function with t ranging from 0 to 1 in iterate_number steps
    points = [bezier(i, control_points) for i in t]

    # show the points, the control points, and time execution
    plt.plot([p[0] for p in points], [p[1] for p in points], 'r-')
    plt.plot([p[0] for p in control_points], [p[1] for p in control_points], 'b-')

    # Calculate execution time
    execution_time = (time.time() - start_time) * 1000

    # Show grid
    plt.title('Brute Force')
    plt.xlabel(f'Execution time: {execution_time:.2f} ms')
    plt.ylabel('Y')
    plt.legend()
    plt.grid(True)

    #plt.show()
# Test the function
# control_points = [(414, 130), (254, 164), (308, 306), (498, 320), (405, 464), (522, 269), (613, 476)]
# iterate_number = 200
# brute_force_process(control_points, iterate_number)

    
