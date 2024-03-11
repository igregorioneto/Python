from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        r = []
        nums.sort()
        for i in range(len(nums)):
            if r.count(nums[i]) < 2:
                r.append(nums[i])
        nums[:] = r
        return len(nums)
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.removeDuplicates(nums = [1,1,1,2,2,3]))