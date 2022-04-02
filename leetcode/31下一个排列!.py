class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left, right = n - 2, n - 1
        while left > 0:
            if nums[left] < nums[left + 1]:
                break
            left -= 1
        while right > 0:
            if nums[right] > nums[left]:
                break
            right -= 1
        nums[left], nums[right] = nums[right], nums[left]
        left = left + 1 if left != right else left
        right = n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


input = [3, 2, 1]
Solution().nextPermutation(input)
print(input)
