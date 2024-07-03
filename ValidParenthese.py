# Leetcode 20. Valid Parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in ['(', '{', '[']:
                stack.append(char)
            else:
                if not stack:
                    return False
                curr_char = stack.pop()
                if curr_char == '(':
                    if char != ')':
                        return False
                if curr_char == '{':
                    if char != '}':
                        return False
                if curr_char == '[':
                    if char != ']':
                        return False

        if stack:
            return False

        return True

if __name__ == "__main__":
    s = Solution()
    print(s.isValid("{[]}"))
