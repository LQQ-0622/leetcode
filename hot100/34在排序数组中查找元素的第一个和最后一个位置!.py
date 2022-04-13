class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        if n == 0 or target < nums[0] or target > nums[n - 1]:
            return [-1, -1]

        def binarySearch(nums, target, lower):
            n = len(nums)
            l, r = 0, n - 1
            ans = n
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] > target or (lower and nums[mid] >= target):
                    r = mid - 1
                    ans = mid
                else:
                    l = mid + 1
            return ans

        left = binarySearch(nums, target, True)
        right = binarySearch(nums, target, False) - 1
        if left <= right and nums[left] == target and nums[right] == target:
            return [left, right]
        return [-1, -1]

    def searchRange1(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        if n == 0 or target < nums[0] or target > nums[n - 1]:
            return [-1, -1]
        left, right = -1, -1
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                left = right = mid
                break
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        if left == -1:
            return [-1, -1]
        while left >= 0 and nums[left] == target: left -= 1
        while right <= n - 1 and nums[right] == target: right += 1

        left = left + 1
        right = right - 1
        return [left, right]


input = [1]
result = Solution().searchRange(input, 1)
print(result)
