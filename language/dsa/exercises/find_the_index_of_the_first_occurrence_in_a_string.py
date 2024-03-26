class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            i = 0
            step = len(needle)
            while i < len(haystack):
                if needle == haystack[i:step]:
                    break
                i += 1
                step += 1
            return i
        return -1
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.strStr(haystack = "sadbutsad", needle = "sad"))  