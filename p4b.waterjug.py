j1 = int(input("Capacity of jug 1: "))
j2 = int(input("Capacity of jug 2: "))
g = int(input("Amount of water to be measured: "))

def apply_rule(ch, x, y):
    if ch == 1:
        if x < j1:
            return j1, y
        else:
            print("Rule cannot be applied")
            return x, y
    elif ch == 2:
        if y < j2:
            return x, j2
        else:
            print("Rule cannot be applied")
            return x, y
    elif ch == 3:
        if x > 0 and x + y <= j2:
            return 0, x + y
        else:
            print("Rule cannot be applied")
            return x, y
    elif ch == 4:
        if y > 0 and x + y <= j1:
            return x + y, 0
        else:
            print("Rule cannot be applied")
            return x, y
    elif ch == 5:
        if x > 0 and x + y >= j2:
            return x - (j2 - y), j2
        else:
            print("Rule cannot be applied")
            return x, y
    elif ch == 6:
        if y > 0 and x + y >= j1:
            return j1, y - (j1 - x)
        else:
            print("Rule cannot be applied")
            return x, y
    elif ch == 7:
        if x > 0:
            return 0, y
        else:
            print("Rule cannot be applied")
            return x, y
    elif ch == 8:
        if y > 0:
            return x, 0
        else:
            print("Rule cannot be applied")
            return x, y
    else:
        print("Invalid choice")
        return x, y

x = y = 0

while True:
    if x == g or y == g:
        print("Goal Achieved!")
        break
    else:
        print("-------------Rules------------")
        print("Rule 1: Fill jug 1")
        print("Rule 2: Fill jug 2")
        print("Rule 3: Transfer all water from jug 1 to jug 2")
        print("Rule 4: Transfer all water from jug 2 to jug 1")
        print("Rule 5: Transfer some water from jug 1 to jug 2 until jug 2 is full")
        print("Rule 6: Transfer some water from jug 2 to jug 1 until jug 1 is full")
        print("Rule 7: Empty jug 1")
        print("Rule 8: Empty jug 2")
        ch = int(input("Enter rule to apply: "))
        x, y = apply_rule(ch, x, y)
        print("----------STATUS--------")
        print("Current State:", end=" ")
        print(x, y)
