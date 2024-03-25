class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        reverse = []
        for i in range(len(arr) - 1, -1, -1):
            reverse.append(arr[i])
        return " ".join(reverse)
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.reverseWords(s = "the sky is blue"))     