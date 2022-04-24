class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSum, pre = nums[0], 0
        for i in nums:
            pre = max(pre + i, i)
            maxSum = max(pre, maxSum)
        return maxSum


input = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
result = Solution().maxSubArray(input)
print(result)
