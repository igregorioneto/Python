class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        str = []
        max, c, i = 0, 0, 0
        while c < len(s):          
            if str.__contains__(s[c]):                
                str[:] = []
                i += 1 
                c = i
                continue
            str.append(s[c])
            if len(str) > max:
                max = len(str)
            c += 1
        return max
    
solution = Solution()
print(solution.lengthOfLongestSubstring(s = "dvdf"))
