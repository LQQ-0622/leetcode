# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int
#

class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left = 0
        lookup = set()
        n = len(s)
        max_len = 0
        cur_len = 0
        for i in range(n):
            cur_len += 1
            while s[i] in lookup:  # 滑动左边窗口直至窗口内没有s[i],再将s[i]加入窗口
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            max_len = max(max_len, cur_len)
            lookup.add(s[i])
        return max_len

    def lengthOfLongestSubstring1(self, s):
        from collections import defaultdict
        lookup = defaultdict(int)
        start = 0
        end = 0
        max_len = 0
        flag = 0  # 窗口内是否有重复标志
        while end < len(s):
            if lookup[s[end]] > 0:
                flag += 1
            lookup[s[end]] += 1
            end += 1
            while flag > 0:  # 滑动左边窗口直至flag=0
                if lookup[s[start]] > 1:
                    flag -= 1
                lookup[s[start]] -= 1
                start += 1
            max_len = max(max_len, end - start)
        return max_len

    def lengthOfLongestSubstring2(self, s):
        if not s:
            return 0
        left, cur_len, max_len = 0, 0, 0
        slide_window = set()
        for i in range(len(s)):
            cur_len += 1
            while s[i] in slide_window:
                slide_window.remove(s[left])
                left += 1
                cur_len -= 1
            slide_window.add(s[i])
            max_len = max(cur_len, max_len)
        return max_len


input = ['a', 'b', 'c', 'c', 'a', 'b', 'd']
result = Solution().lengthOfLongestSubstring2(input)
print(result)
