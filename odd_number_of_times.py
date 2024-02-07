def odd_number_of_times(arr):
    odd_set = set()
    for i in arr:
        if i in odd_set:
            odd_set.remove(i)
        else:
            odd_set.add(i)
    return odd_set

arr = [1, 4, 5, 2, 7, 8, 3, 4, 5, 1, 2, 8, 3,6,9]
print(odd_number_of_times(arr))  # 7

