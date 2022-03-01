class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        l = []
        for i in range(len(nums)):
            if nums.count(nums[i]) == 1:
                l.append(nums[i])
            if len(l) == 2:
                return l
            