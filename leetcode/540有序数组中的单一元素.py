class Solution:
    def singleNonDuplicate(self, nums):
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] == nums[mid ^ 1]:
                low = mid + 1
            else:
                high = mid
        return nums[low]


input = [1, 1, 2, 2, 3, 4, 4, 5, 5]
result = Solution().singleNonDuplicate(input)
print(1)