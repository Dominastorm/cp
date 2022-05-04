class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        start = 0
        end = len(nums)-1
        res = 0
        while start < end:
            if nums[start] + nums[end] > k:
                end -= 1
            elif nums[start] + nums[end] == k:
                res += 1
                start += 1
                end -= 1
            else:
                start += 1
        return res