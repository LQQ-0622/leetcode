class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        result = list()
        for first in range(n):  # 枚举a
            if first > 0 and nums[first] == nums[first - 1]:  # 排除和上次枚举相同的数a
                continue
            target = -nums[first]  # 当a确定时，找到b+c=-a(target)
            third = n - 1  # c对应的指针初始指向数组最大值
            for second in range(first + 1, n):
                if second > first + 1 and nums[second] == nums[second - 1]:  # 排除和上次枚举相同的数b
                    continue
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                if second == third:  # 如果指针重合，随着 b 后续的增加。就不会有满足 a+b+c=0 并且 b<c 的 c 了，可以退出循环
                    break
                if nums[second] + nums[third] == target:
                    result.append([nums[first], nums[second], nums[third]])
        return result

    def threeSum2(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        result = list()
        for first in range(n - 2):  # 枚举a
            if first > 0 and nums[first] == nums[first - 1]:  # 排除和上次枚举相同的数a
                continue
            target = -nums[first]  # 当a确定时，找到b+c=-a(target)
            second = first + 1
            third = n - 1  # c对应的指针初始指向数组最大值
            while second < third:
                if nums[second] + nums[third] > target:
                    third -= 1
                if nums[second] + nums[third] < target or (
                        nums[second] == nums[second - 1] and second > first + 1):  # 第二个条件用来排除和上次枚举相同的数b
                    second += 1
                elif nums[second] + nums[third] == target and second != third:
                    result.append([nums[first], nums[second], nums[third]])
                    second += 1  # 继续找下一种情况，直到second = third。（当a确定时，有可能存在多种可能性使得b+c=-a）
        return result


input = [-1, 0, 1, 2, -1, -4]
result = Solution().threeSum2(input)
print(result)
