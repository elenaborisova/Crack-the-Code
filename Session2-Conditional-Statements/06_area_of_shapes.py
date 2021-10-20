import math

type = input("Is the geometric figure a: square, rectangle, circle or triangle? ").casefold()

if type == "square":
    side = float(input())
    print(side * side)
elif type == "rectangle":
    side_a = float(input())
    side_b = float(input())
    print(side_a * side_b)
elif type == "circle":
    r = float(input())
    print(round(r * r * math.pi, 2))
else:
    side = float(input())
    h = float(input())
    print((h * side) / 2)
