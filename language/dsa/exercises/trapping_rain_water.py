from typing import List

class Solution:
    def trap2(self, height: List[int]) -> int:
        water = 0
        for i in range(1, len(height)):
            min_height = min(max(height[0:i]), max(height[i:len(height)]))
            if (min_height - height[i]) > 0:
                water += (min_height- height[i])
        return water
    
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n

        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])

        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        water = 0
        for i in range(n):
            water += min(left_max[i], right_max[i]) - height[i]
            
        return water
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.trap(height = [0,1,0,2,1,0,1,3,2,1,2,1]))