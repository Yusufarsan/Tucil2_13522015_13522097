# ini file untuk memanggil semua fungsi dari file lain
# file ini sebagai program utama yang akan dijalankan

from masukkan import get_input_terminal, get_input_file
from brute_force import brute_force_process
from DivideAndConquer import divideAndConquer
import matplotlib.pyplot as plt

print('''Welcome to Bezier Curve Visualization Program
made by:
13522015 - Yusuf Ardian Sandi
13522097 - Ellijah Darrellshane Suryanegara
      
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

x_values1 = [point[0] for point in control_points]
y_values1 = [point[1] for point in control_points]
plt.subplot(2, 2, 1)

# Plotting both graphs on a single figure
plt.plot(x_values1, y_values1, marker='.', label='Initial Graph')
plt.pause(0.5)
divideAndConquer(control_points, iterate_number, 1)

plt.subplot(2, 2, 2)
plt.plot(x_values1, y_values1, label='Initial Graph')
# Add labels and legend
plt.title('Result')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)

plt.subplot(2, 2, 3)
brute_force_process(control_points, iterate_number)

# Display the combined graph
plt.suptitle('Bezier Curve')
plt.tight_layout()
plt.show()
