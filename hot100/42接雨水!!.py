class Solution:
    def trap(self, height: list[int]) -> int:
        left, right, maxLeft, maxRight, result = 0, len(height) - 1, 0, 0, 0
        while left < right:
            maxLeft = max(height[left], maxLeft)
            maxRight = max(height[right], maxRight)
            if height[left] < height[right]:
                result += maxLeft - height[left]
                left += 1
            else:
                result += maxRight - height[right]
                right -= 1
        return result


input = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
input = [4, 2, 0, 3, 2, 5]
# input = [4, 2, 3]
result = Solution().trap(input)
print(result)
