"""
找出数组中重复的数字。

在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。
数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。
请找出数组中任意一个重复的数字。

示例 1：
输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3
"""


class Solution:
    # 时间:O(n), 空间:O(1)
    def findRepeatNumber1(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 0:  # 判断数组非空
            return False
        for i in nums:  # 判断数组中的数组在0~n-1之间
            if i >= n:
                return False
        for i in range(n):
            while nums[i] != i:
                if nums[nums[i]] == nums[i]:
                    return nums[i]
                temp = nums[i]
                nums[i], nums[temp] = nums[temp], nums[i]

    # 哈希，时间:O(n), 空间:O(n)
    def findRepeatNumber2(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 0:
            return False
        for i in nums:
            if i >= n:
                return False
        replaceSet = set()
        for num in nums:
            if num not in replaceSet:
                replaceSet.add(num)
            else:
                return num


nums = [2, 3, 1, 0, 1000, 2, 5, 3]
# nums = [2, 3, 1, 0, 2, 5, 3]
repeated_num = Solution().findRepeatNumber1(nums)
print(repeated_num)
