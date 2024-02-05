def contains_all_in_range(arr, A, B):
    range_set = set(range(A, B+1))

    array_set = set(arr)
    return range_set.issubset(array_set)

arr = [1, 4, 5, 2, 7, 8, 3]
A = 2
B = 5
print(contains_all_in_range(arr, A, B))  #
