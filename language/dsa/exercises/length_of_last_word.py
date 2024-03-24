class Solution:
    def lengthOfLastWord2(self, s: str) -> int:
        return len(s.strip().split(" ")[-1])
    
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        i = len(s) - 1
        while i >= 0 and s[i] == " ":
            i -= 1

        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1

        return length

if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLastWord(s = "   fly me   to   the moon  "))     