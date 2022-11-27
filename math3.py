from math import tan, pi

num_of_sides, length = int(input('Input number of sides: ')), int(input('Input the length of a side: '))
area = int(num_of_sides * (length**2) / (4*tan(pi / num_of_sides)))

print(area)