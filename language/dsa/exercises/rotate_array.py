from typing import List

class Solution:
    def rotate3(self, nums: List[int], k: int) -> None:
        r = []
        while k > 0:
            r.append(nums[-1])
            for num in nums[:-1]:
                r.append(num)
            nums[:] = r
            r = []
            k -= 1


        return 0
    
    def rotate2(self, nums: List[int], k: int) -> None:
        if k == 0:
            return
        elif len(nums) > k:
            nums[:] = nums[-k:] + nums[:(len(nums) - k)]
        else:
            for i in range(k):
                rotation = nums[:-1]
                rotation.insert(0, nums[-1])
                nums[:] = rotation

        return 0
    
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        def reverse(i: int, j: int) -> None:
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
            print(f"Reverse {nums}")

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)

        print(nums)

        return 0



if __name__ == "__main__":
    solution = Solution()
    print(solution.rotate(nums = [1,2,3,4,5,6,7], k = 3))