def reverse_seq(n):
    array = []
    for x in range(n, 0, -1):
      array.append(x)
    return array

reverse = lambda n: [n for n in range(n, 0, -1)]
print(reverse(5))