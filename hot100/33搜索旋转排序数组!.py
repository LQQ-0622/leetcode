class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:  # nums[l]也可为nums[0]
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:  # nums[r]也可为nums[len(nums)-1]
                    l = mid + 1
                else:
                    r = mid - 1
        return -1


input = [4, 5, 6, 7, 8, 9, 1, 2, 3]
result = Solution().search(input, 2)
print(result)
