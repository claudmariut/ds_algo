# 3 constant assignments.
a = 5
b = 6
c = 10

# 3n^2 assignments. Or n*n*3.
for i in range(n):
    for j in range(n):
        x = i * i
        y = j * j
        z = i * j

# 2n assignments.
for k in range(n):
    w = a * k + 45
    v = b * b

# 1 constant.
d = 33

# T(n) = O(n^2).

