def hinh1(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
def hinh2(n):
    for i in range(1, n+1):
        print("* " * i)
def hinh3(n):
    for i in range(1, n+1):
        print("  " * (n-i) + "* " * i)

n = 5
print("Hình 1:")
hinh1(n)

print("\nHình 2:")
hinh3(n)

print("\nHình 3:")
hinh2(n)


