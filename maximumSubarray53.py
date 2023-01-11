class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsub = nums[0]
        currentSum =0

        for n in nums:
            if currentSum < 0:
                currentSum=0
            currentSum= currentSum+n
            maxsub = max(maxsub, currentSum)
        return maxsub
