from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        max_index = len(citations)
        for i in citations:
            if i < max_index:
                max_index -= 1
            else:
               return max_index
        return max_index

    
if __name__ == "__main__":
    solution = Solution()
    print(solution.hIndex(citations = [3,0,6,1,5]))