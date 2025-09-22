width = 11
rows = [1, 3, 7, 3, 5, 11, "two", "two"]

for i, r in enumerate(rows, start=1):
    if r == "two":
        stars = "* *"
        padding = (width - len(stars)) // 2
        line = " " * padding + stars
    else:
        padding = (width - r) // 2
        line = " " * padding + "*" * r
    print(f"row {i} : {line}")
