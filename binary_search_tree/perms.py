def perms(string):
    """Return list of perms of string"""

    if string == "":
        return ""

    if len(string) == 1:
        return [string]

    else:
        l = []

    for index in range(len(string)):
        main = string[index]
        rest = string[index + 1:] + string[:index]

        for x in perms(rest):
            l.append(main + x)

    return l


def findLexicographicPerm(string):
    alist = perms(string)
    alist.sort()
    return alist[999_999]


print(findLexicographicPerm("0123456789"))