n = int(input())
max_num = -10000000000000
min_num = 10000000000000

for i in range(1, n + 1):
    num = int(input())
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

print(f"Max number: {max_num}")
print(f"Min number: {min_num}")

