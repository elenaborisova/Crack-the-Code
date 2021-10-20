import math
type = input("Is the geometric figure a: 'square', 'rectangle', 'circle' or 'triangle? ").casefold()

if type == 'square':
    side = float(input("Side: "))
    print(side * side)
elif type == 'rectangle':
    sideA = float(input("Side A: "))
    sideB = float(input("Side B: "))
    print(sideA * sideB)
elif type == 'circle':
    r = float(input("Radius: "))
    print(round(r * r * math.pi, 2))
else: # 'triangle'
    sideB = float(input("Side B: "))
    h = float(input("h: "))
    print((h * sideB) / 2)