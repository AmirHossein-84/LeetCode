class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        sum = nums[0]
        for i in range(len(nums) -1):
            if sum + nums[i + 1] < nums[i + 1]:
                sum = nums[i + 1]
            else:
                sum += nums[i + 1]
            max_sum = max(max_sum, sum)
        return max_sum