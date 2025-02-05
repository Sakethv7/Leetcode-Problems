class Solution:
    def uniqueLetterString(self, s: str) -> int:
        n = len(s)
        # Arrays to store distances:
        # left[i] = number of ways to choose a start index that makes s[i] the first occurrence in the substring.
        # right[i] = number of ways to choose an end index that makes s[i] the last occurrence in the substring.
        left = [0] * n
        right = [0] * n

        # For each character, find the distance from its previous occurrence.
        prev_occ = {}
        for i in range(n):
            if s[i] in prev_occ:
                left[i] = i - prev_occ[s[i]]
            else:
                left[i] = i + 1  # All positions [0, i] are valid if there's no previous occurrence.
            prev_occ[s[i]] = i

        # Similarly, traverse backwards to find the distance to the next occurrence.
        next_occ = {}
        for i in range(n - 1, -1, -1):
            if s[i] in next_occ:
                right[i] = next_occ[s[i]] - i
            else:
                right[i] = n - i  # All positions [i, n-1] are valid if there's no next occurrence.
            next_occ[s[i]] = i

        # Sum up the contributions: each s[i] contributes left[i] * right[i]
        result = 0
        for i in range(n):
            result += left[i] * right[i]
        return result