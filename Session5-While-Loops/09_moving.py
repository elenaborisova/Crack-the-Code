free_width = int(input())
free_length = int(input())
free_height = int(input())

free_space = free_width * free_length * free_height
box_space = 0

line = input()
while line != "Done":
    boxes = int(line)
    box_space += boxes

    if box_space > free_space:
        print(f"No more free space! You need {box_space - free_space} Cubic meters more.")
        break

    line = input()

if free_space > box_space:
    print(f"{free_space - box_space} Cubic meters left.")
