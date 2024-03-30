class Solution:
    def isSubsequence2(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)

    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for char in t:
            if i < len(s) and char == s[i]:
                i += 1
        return i == len(s)
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.isSubsequence(s = "ace", t = "abcde"))