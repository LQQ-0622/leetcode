class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        result = []

        def backtrace(index):
            if index == n:
                result.append(nums[:])
            for i in range(index, n):
                nums[i], nums[index] = nums[index], nums[i]
                backtrace(index + 1)
                nums[i], nums[index] = nums[index], nums[i]

        backtrace(0)
        return result


input = [1, 2, 3, 4]
result = Solution().permute(input)
print(result)
