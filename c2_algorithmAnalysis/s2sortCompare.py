# Sorting and compare. Looks like O(n), but sorting two list, can be either
# O(n^2) or O(nlogn)


def anagramSolution2(s1="earth", s2="heart"):
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if alist1[pos] == alist2[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches


