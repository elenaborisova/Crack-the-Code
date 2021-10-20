num = input()
max_num = -1000000000000

while num != "Stop":
    num = int(num)
    if num > max_num:
        max_num = num

    num = input()

print(max_num)
