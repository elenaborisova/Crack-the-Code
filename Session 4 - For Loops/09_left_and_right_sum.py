n = int(input())

left_sum = 0
right_sum = 0

for i in range(1, (2 * n) + 1):
    if i <= (n*2)/2:
        left_sum += int(input())
    else:
        right_sum += int(input())


if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {abs(left_sum - right_sum)}")

