hour = int(input())
day = input()

if 10 <= hour < 18 and (day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday" or day == "Saturday"):
    print("open")
elif hour < 10 or hour >= 18 or day == "Sunday":
    print("closed")