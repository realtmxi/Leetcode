class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        result = 0
        negative = False
        for i in range(len(s)):
            # if s[i] == " ":
            #     continue
            if i == 0 and s[i] == '+':
                continue
            elif i == 0 and s[i] == '-':
                negative = True
            elif result == 0 and s[i] == '0':
                continue
            elif s[i] not in '0123456789':
                break
            else:
                result = result * 10 + int(s[i])

        if negative:
            result *= -1
        if result > 2 ** 31 - 1:
            result = 2 ** 31 - 1
        elif result < - 2 ** 31:
            result = 2 ** 31 * -1

        return result


if __name__ == '__main__':
    s = Solution()
    print(s.myAtoi("   +0 123"))
