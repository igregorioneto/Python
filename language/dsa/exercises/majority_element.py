from typing import List


class Solution:
    def majorityElement2(self, nums: List[int]) -> int:
        more = len(nums) / 2
        e = 0
        nums.sort()
        for x in range(len(nums)):
            if nums.count(nums[x]) > more:
                e = nums[x]
                break
        return e
    
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1
            if count[num] >= len(nums) / 2:
                return num
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.majorityElement(nums = [2,2,1,1,1,2,2]))