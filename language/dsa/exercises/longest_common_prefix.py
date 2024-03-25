from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        n = 1000
        for st in strs:
            if len(st) < n:
                n = len(st)

        is_prefix = False        
        
        for i in range(1,n + 1):
            sub = strs[0][0:i]
            for p in strs:
                if sub == p[0:i]:
                    is_prefix = True
                    continue
                else:
                    is_prefix = False
                    break
            if is_prefix:
                prefix = sub
        return prefix
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.longestCommonPrefix(strs = ["flower","flower","flower","flower"]))