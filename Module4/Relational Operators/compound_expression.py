MAX = 10
MIN = 0
y = 5

if y > MAX:
    print("Y is greater than ", MAX)

if y < MIN:
    print("Y is less than ",  MIN)

x = 5

if x > MIN and x < MAX:
    print("X is between MAX and MIN")

if x >= MIN and x < MAX:
    print("X in greater than equal to the MIN but less than the MAX")

if x > MIN and x <= MAX:
    print("X is greater than MIN but is less than or equal to MAX")
