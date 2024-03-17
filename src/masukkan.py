# ini file untuk nge handle inputan

from typing import List

def get_control_points() -> List[tuple[int, int]]:
    '''Get the control points from the user input'''
    control_points = []
    n = int(input("Enter the number of control points: "))
    print()
    for i in range(n):
        x = int(input(f"Enter x{i+1}: "))
        y = int(input(f"Enter y{i+1}: "))
        print()
        control_points.append((x, y))
    return control_points

def get_iterate_number() -> int:
    '''Get the iterate number from the user input'''
    iterate_number = int(input("Enter the iterate number: "))
    print()
    return iterate_number

def get_input_terminal() -> tuple[List[tuple[int, int]], int]:
    '''Get the control points and iterate number from the user input'''
    control_points = get_control_points()
    iterate_number = get_iterate_number()
    return control_points, iterate_number

def get_input_file() -> tuple[List[tuple[int, int]], int]:
    '''Get the control points and iterate number from the input file'''
    control_points = []
    iterate_number = 0
    filename = input("Enter the file name without extension: ")
    with open(f"../test/{filename}.txt", "r") as file:
        n = int(file.readline())
        iterate_number = int(file.readline())
        for i in range(n):
            x, y = map(int, file.readline().split())
            control_points.append((x, y))
    return control_points, iterate_number
# File txt example:
# 3 <- number of control points
# 100 <- iterate number
# 0 0 <- control point 1
# 5 10 <- control point 2
# 10 5 <- control point 3