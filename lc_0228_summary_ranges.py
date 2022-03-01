class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        if nums:
            low = nums[0]
            high = nums[0]
        i = 0
        while i < len(nums):
            if i < len(nums) -1 and nums[i+1] == nums[i] + 1:
                high += 1
            elif low == high:
                ans.append(str(low))
                if i != len(nums)-1:
                    low = nums[i+1]
                    high = nums[i+1]
            else:
                ans.append(str(low)+"->"+str(high))
                if i != len(nums)-1:
                    low = nums[i+1]
                    high = nums[i+1]
            i += 1
        return ans