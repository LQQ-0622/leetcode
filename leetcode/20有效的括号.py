class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        stack = []
        match = {
            '}': '{',
            ')': '(',
            ']': '['
        }
        for ch in s:
            if ch in match:
                if not stack or stack[-1] != match[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return not stack

    def isValid1(self, s: str) -> bool:
        stack = []
        stack.append(s[0])
        for i in range(1, len(s)):
            if s[i] in ['(', '[', '{']:
                stack.append(s[i])
            elif stack == []:
                return False
            elif s[i] == ')' and stack[-1] == '(':
                stack.pop()
            elif s[i] == ']' and stack[-1] == '[':
                stack.pop()
            elif s[i] == '}' and stack[-1] == '{':
                stack.pop()
            else:
                return False
        if stack == []:
            return True
        else:
            return False
