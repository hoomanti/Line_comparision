# assigning value to first line
import math

x1, x2, y1, y2 = 3, 8, 4, 9

# assigning value to second line
p1, p2, q1, q2 = 8, 13, 10, 12

# calculate length of both the lines
length_of_line1 = math.sqrt(((y2 - y1) * (y2 - y1) + (x2 - x1) * (x2 - x1)))
print(length_of_line1)
length_of_line2 = math.sqrt(((q2 - q1) * (q2 - q1) + (p2 - p1) * (p2 - p1)))
print(length_of_line2)
if length_of_line1 is length_of_line2:
    print("Length of both the lines are equal.")
elif length_of_line1 < length_of_line2:
    print("Second line is greater than first line.")
else:
    print("First line is greater than second line.")
