# Determine how many palindromic subsequences of length k in s
def solve(s, k):
	if k == 0:
		return 1
	if k == 1:
		return len(set(s))

	result = 0
	letters = set(s)
	for letter in letters:
		start = s.index(letter)
		end = s.rindex(letter)
		if start < end:
			result += solve(s[start + 1: end], k - 2)

	return result

print(solve("abbbabba", 5))

