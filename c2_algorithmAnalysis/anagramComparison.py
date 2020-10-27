from timeit import Timer


s1 = Timer("anagramSolution1()", "from s1checkingOff import anagramSolution1")
print("Checking Off : ", s1.timeit(number=1000), "miliseconds")
s2 = Timer("anagramSolution2()", "from s2sortCompare import anagramSolution2")
print("Sort and Compare: ", s2.timeit(number=1000), "miliseconds")
s3 = Timer("anagramSolution3()", "from s3bruteForce import anagramSolution3")
print("Brute Force: ", s3.timeit(number=1000), "miliseconds")
s4 = Timer("anagramSolution4()", "from s4countCompare import anagramSolution4")
print("Count and Compare: ", s4.timeit(number=1000), "miliseconds")
