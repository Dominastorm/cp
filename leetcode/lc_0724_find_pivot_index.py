class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums[1:])
        for i in range(len(nums)):
            if left_sum == right_sum:
                return i
            curr = nums[i]
            if i != len(nums) - 1:
                next = nums[i + 1]
            left_sum += curr
            right_sum -= next
        return -1
            
        