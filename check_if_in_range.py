def contains_all_in_range(arr, A, B):
    range_set = set(range(A, B+1))

    array_set = set(arr)
    return range_set.issubset(array_set)

arr = [1, 4, 5, 2, 7, 8, 3]
A = 2
B = 5
print(contains_all_in_range(arr, A, B))  #


class Solution:
    def check_elements(self, arr, n, A, B):
        # Create a set of all numbers in the range
        range_set = set(range(A, B+1))

        # Create a set of all numbers in the array
        arr_set = set(arr)

        # Check if the array set contains all numbers in the range set
        return range_set.issubset(arr_set)

# Test the method
s = Solution()
arr = [1, 4, 5, 2, 7, 8, 3]
n = len(arr)
A = 2
B = 5
print(s.check_elements(arr, n, A, B))  # Prints True




def checks_element(arr, A, B):

    array_set = set(arr)
    range_set = set(range(A, B+1))
    return range_set.issubset(array_set)
A = 2
B = 5

arr = [1, 4, 5, 2, 7, 8, 3]

print(checks_element(arr, A, B))  