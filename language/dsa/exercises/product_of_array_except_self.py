from typing import List

class Solution:
    def productExceptSelf3(self, nums: List[int]) -> List[int]:
        product = 1
        r = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j != i:
                    product *= nums[j]
            r.append(product)
            product = 1
        return r
    
    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        product = 1
        r = []
        i = 0
        n = len(nums)
        lenght = 0
        while True:
            if lenght == n:
                r.append(product)
                i += 1
                product = 1
                lenght = 0

            if i == n:
                break

            if i != lenght:
                product *= nums[lenght]

            lenght += 1

        return r
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        zero_count = 0

        for num in nums:
            if num != 0:
                total_product *= num
            else:
                zero_count += 1

        result = []

        if zero_count > 1:
            return [0] * len(nums)
        
        for num in nums:
            if num != 0:
                if zero_count == 1:
                    result.append(0)
                else:
                    result.append(total_product // num)
            else:
                result.append(total_product)
        
        return result
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.productExceptSelf(nums = [1,2,3,4]))