digitize = lambda n: [int(x) for x in list(str(n))[::-1]]
print(digitize(35231))