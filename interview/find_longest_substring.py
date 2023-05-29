# 数蓬科技 nlp算法工程师 面试
def len_longest_substring(s):
	start = 0
	max_len = 0
	used_char = {}

	for i in range(len(s)):
		if s[i] in used_char and start <= used_char[s[i]]:
			start = used_char[s[i]] + 1
		else:
			max_len = max(max_len, i - start + 1)

		used_char[s[i]] = i

	return max_len


if __name__ == "__main__":
	s1 = "abcabcbb"
	s2 = "bbbbb"
	s3 = "pwwkew"
	print(len_longest_substring(s1))
	print(len_longest_substring(s2))
	print(len_longest_substring(s3))
