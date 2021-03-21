"""
CP1404/CP5632 - Practical
Loops
"""
print("Given Loop: ")
for i in range(1, 21, 2):
    print(i, end=' ')
print()

print("Part A: ")
for i in range(0, 101, 10):
    print(i, end=' ')
print()

print("Part B ")
for i in range(20, 0, -1):
    print(i, end=' ')
print()

print("Part C ")
print("Number of stars: ")
choice = int(input(">>> "))
for i in range(0, choice, 1):
    print("*", end='')
print()

print("Part D ")
print("Number of stars: ")
choice = int(input(">>> "))
timer = 1
for i in range(0, choice, 1):
    print()
    for j in range(0, timer, 1):
        print("*", end='')
    timer += 1
print()

