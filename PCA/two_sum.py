class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            remaining = target - num
            if remaining in seen:
                return [seen[remaining], i]
            seen[num]= i
        return []