def cycle_array(arr):
    popped_element = arr.pop()
    arr.insert(0, popped_element)


arr = [1, 2, 3, 4, 5]
cycle_array(arr)
print(arr)