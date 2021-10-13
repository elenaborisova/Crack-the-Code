balance = 0

line = input()
while line != "NoMoreMoney":
    current_amount = float(line)

    if current_amount < 0:
        print("Invalid operation!")
        break

    print(f"Increase: {current_amount:.2f}")
    balance += current_amount

    line = input()

print(f"Total: {balance:.2f}")
