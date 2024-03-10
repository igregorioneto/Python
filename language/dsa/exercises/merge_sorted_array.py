from typing import List

class Solution:
    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int ) -> None:
        result = []
        for n1 in range(m):
            result.append(nums1[n1])

        for n2 in range(n):
            result.append(nums2[n2])

        result.sort() 
        nums1 = result

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        if n == 0: return
        len1 = len(nums1)
        end_idx = len1 - 1

        while n > 0 and m > 0:
            if nums2[n - 1] >= nums1[m - 1]:
                nums1[end_idx] = nums2[n - 1]
                n -= 1
            else:
                nums1[end_idx] = nums1[m - 1]
                m -= 1
            end_idx -= 1

        while n > 0:
            nums1[end_idx] = nums2[n - 1]
            n -= 1
            end_idx -= 1            


if __name__ == "__main__":
    solution = Solution()
    solution.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)