from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxArea = 0

        while left < right:
            currentArea = min(height[left], height[right]) * (right - left)
            maxArea = max(maxArea, currentArea)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea
    

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxArea(height = [1,8,6,2,5,4,8,3,7]))