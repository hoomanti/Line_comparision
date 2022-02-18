# assigning value to first line
import math

x1, x2, y1, y2 = 3, 8, 4, 9

# assigning value to second line
p1, p2, q1, q2 = 12, 17, 13, 18

# calculate length of both the lines
length_of_line1 = math.sqrt(((y2 - y1) * (y2 - y1) + (x2 - x1) * (x2 - x1)))
print(length_of_line1)
length_of_line2 = math.sqrt(((q2 - q1) * (q2 - q1) + (p2 - p1) * (p2 - p1)))
print(length_of_line2)

if length_of_line1 == length_of_line2:
    print("Length of both the lines are equal")
