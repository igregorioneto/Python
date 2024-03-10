from typing import List

class Solution:
    def removeElement2(self, nums: List[int], val: int) -> int:
        if val == 0: return

        n = len(nums) - 1
        result = []
        while n >= 0:
            if nums[n] != val:
                result.append(nums[n])
            n -= 1

        n2 = len(result) - 1
        n = len(nums) - 1
        while n2 < n:
            result.append(0)
            n2 += 1
        
        return val
    
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i

if __name__ == "__main__":
    solution = Solution()
    print(solution.removeElement(nums = [3,2,2,3], val = 3))