class Solution:
    # Two window pointer
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        length = 0
        for r in range(len(s)):
            char = s[r]
            if char in seen and seen[char] >= 1:
                l = seen[char] + 1
            else:
                length = max(length, r - l + 1)
                seen[char] = r
        return length


if __name__ == "__main__":
    solution = Solution()
    s = "aux"
    print(solution.lengthOfLongestSubstring(s))
