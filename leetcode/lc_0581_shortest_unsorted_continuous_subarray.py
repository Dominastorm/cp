class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        res = len(nums)
        start = 0
        while start < len(nums)-1:
            if nums[start] <= min(nums[start+1:]):
                res -= 1
                start += 1
            else:
                break
        else:
            return 0
        i = len(nums)-1
        while i > start:
            if nums[i] >= max(nums[:i]):
                res -= 1
                i -= 1
            else:
                break
        return res