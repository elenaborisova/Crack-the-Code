product = input()
city = input()
amount = float(input())

price = 0

if city == "Sofia":
    if product == "coffee":
        price = 0.50 * amount
        print(price)
    elif product == "water":
        price = 0.80 * amount
        print(price)
    elif product == "beer":
        price = 1.20 * amount
        print(price)
    elif product == "sweets":
        price = 1.45 * amount
        print(price)
    elif product == "peanuts":
        price = 1.60 * amount
        print(price)
elif city == "Plovdiv":
    if product == "coffee":
        price = 0.40 * amount
        print(price)
    elif product == "water":
        price = 0.70 * amount
        print(price)
    elif product == "beer":
        price = 1.15 * amount
        print(price)
    elif product == "sweets":
        price = 1.30 * amount
        print(price)
    elif product == "peanuts":
        price = 1.50 * amount
        print(price)
elif city == "Varna":
    if product == "coffee":
        price = 0.45 * amount
        print(price)
    elif product == "water":
        price = 0.70 * amount
        print(price)
    elif product == "beer":
        price = 1.10 * amount
        print(price)
    elif product == "sweets":
        price = 1.35 * amount
        print(price)
    elif product == "peanuts":
        price = 1.55 * amount
        print(price)