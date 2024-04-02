from typing import List

class Solution:
    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        r = set()
        nums.sort()
        n = len(nums)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        r.add((nums[i], nums[j], nums[k]))
        return r
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        n = len(nums)
        
        for i in range(n - 2):
            # Evita repetição de valores fixos
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])

                    # Evita repetição dos valores dos ponteiros
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                    
        return result    


    
if __name__ == "__main__":
    solution = Solution()
    print(solution.threeSum(nums = [-1,0,1,2,-1,-4]))