def sum_two_smallest_numbers(numbers):
    list = numbers
    p = min(list)
    list.remove(p)
    s = min(list)
    return p + s
print(sum_two_smallest_numbers([19, 5, 42, 2, 77]))

sum_two_smallest_numbers2 = lambda numbers: sum(sorted(numbers)[:2])
print(sum_two_smallest_numbers2([19, 5, 42, 2, 77]))