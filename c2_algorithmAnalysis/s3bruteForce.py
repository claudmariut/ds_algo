# Brute Force. O(n!)
"""
Brute force tries to exhaust all possibilities. There are n factorial possibilites
to rearrange n digits on a string or an integer. This is not a good solution.
"""


def anagramSolution3(s1="earth"):
    if len(s1) == 0:
        return ""
    if len(s1) == 1:
        return s1
    l = []
    for digit in range(len(s1)):
        first = s1[digit]
        rem = s1[:digit:] + s1[digit + 1:]

        for perm in anagramSolution3(rem):
            l.append(first + str(perm))

    return l


if "heart" in anagramSolution3():
    pass
else:
    pass

