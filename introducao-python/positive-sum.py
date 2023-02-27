def positive_sum(arr):
    sum = 0
    for value in arr:
        if value > 0:
            sum += value
    return sum
            
print(positive_sum([1,-4,7,12]))

positive =lambda arr: sum(n for n in arr if n > 0)
print(positive([1,-4,7,12]))

positive2 = lambda arr: sum(filter(lambda n: n > 0, arr))
print(positive2([1,-4,7,12]))