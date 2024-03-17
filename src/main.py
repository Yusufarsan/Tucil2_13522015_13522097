# ini file untuk memanggil semua fungsi dari file lain
# file ini sebagai program utama yang akan dijalankan

from src.masukkan import get_input_terminal, get_input_file
from src.brute_force import brute_force_process

print('''Welcome to Bezier Curve Visualization Program
made by:
13522015 - Yusuf Ardian Sandi
13522097 - Ellijiah DarrelShane
      
Choose the input method:
1. Terminal
2. File
''')

# Get the input method from the user
input_method = int(input("Enter the input method: "))
print()

# Get the control points and iterate number from the user input
if input_method == 1:
    control_points, iterate_number = get_input_terminal()
else:
    control_points, iterate_number = get_input_file()

# Get process method from the user
print('''Choose the process method:
1. Brute Force
2. Divide and Conquer
''')
process_method = int(input("Enter the process method: "))
print()

# Process the brute force method
if process_method == 1:
    brute_force_process(control_points, iterate_number)
else:
    print("Error: Divide and Conquer process method is not available")
