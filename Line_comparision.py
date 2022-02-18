import math

x_coordinate1, x_coordinate2, y_coordinate1, y_coordinate2 = 1, 5, 2, 6
length_of_line = math.sqrt(((y_coordinate2 - y_coordinate1) * (y_coordinate2 - y_coordinate1) +
                            (x_coordinate2 - x_coordinate1) * (x_coordinate2 * x_coordinate1)))
print(length_of_line)

