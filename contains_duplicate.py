

class Solution:
    def containsDuplicate(self, nums) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
        