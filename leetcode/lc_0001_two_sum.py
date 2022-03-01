class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            n1 = nums[i]
            n2 = target-n1
            if n2 in nums:
                j = nums.index(n2)
                if i != j:
                    return [i, j]