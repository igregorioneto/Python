from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        r = []
        for j in range(len(nums)):
            if not r.__contains__(nums[j]):
                r.append(nums[j])        
        r.sort()
        nums[:] = r
        return len(r)

if __name__ == "__main__":
    solution = Solution()
    print(solution.removeDuplicates(nums = [1,1,2]))