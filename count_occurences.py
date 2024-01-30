class Solution(object):
    def topKFrequent(self, nums, k):
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        return [key for key, value in sorted(count.items(), key=lambda item: item[1], reverse= True)[:k]]
    
