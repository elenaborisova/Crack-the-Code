name = input()
average_grade = 0
year = 1
is_excluded = False

while year <= 12:
    grade = float(input())

    if grade < 4:
        if is_excluded:
            break

        is_excluded = True
        continue

    average_grade += grade
    year += 1


if year >= 12:
    print(f"{name} graduated. Average grade: {(average_grade / 12):.2f}")
else:
    print(f"{name} has been excluded at {year} grade")
