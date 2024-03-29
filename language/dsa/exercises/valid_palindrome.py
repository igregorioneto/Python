class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ''
        for char in s:
            if char.isalnum():
                result += char
        result = result.lower()
        return result == result[::-1]

if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome(s = "race a car"))