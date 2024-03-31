from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(numbers):
            complement = target - num
            if complement in seen:
                return [seen[complement] + 1, i + 1]
            seen[num] = i
        return []
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum(numbers = [5,25,75], target = 100))