class Solution:
    def romanToInt(self, s: str) -> int:
        values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        result = 0
        count = len(s)
        i = 0
        while i < count:
            if i < count - 1 and values[s[i]] < values[s[i + 1]]:
                result += (values[s[i + 1]] - values[s[i]])
                i += 2
            else:    
                result += values[s[i]]    
                i += 1
        return result

if __name__ == "__main__":
    solution = Solution()
    print(solution.romanToInt(s = "LXIII"))