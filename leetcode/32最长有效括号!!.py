class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxlen = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack == []:
                    stack.append(i)
                else:
                    maxlen = max(maxlen, i - stack[-1])
            print(i)
        return maxlen

    def longestValidParentheses1(self, s: str) -> int:
        maxlen = 0
        left_num = right_num = 0
        for i in range(len(s)):
            if s[i] == '(':
                left_num += 1
            else:
                right_num += 1
            if left_num == right_num:
                maxlen = max(maxlen, right_num * 2)
            elif right_num > left_num:
                left_num = right_num = 0
        left_num = right_num = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '(':
                left_num += 1
            else:
                right_num += 1
            if left_num == right_num:
                maxlen = max(maxlen, right_num * 2)
            elif right_num < left_num:
                left_num = right_num = 0
        return maxlen


input = "())((())))"
result = Solution().longestValidParentheses1(input)
print(result)
