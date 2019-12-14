'''
88. 合并两个有序数组
'''
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 使用插入排序的变体
        for j in range(n):
            i = j + m - 1
            val = nums2[j]
            while i >= 0 and val < nums1[i]:
                nums1[i+1] = nums1[i]
                i -= 1
            nums1[i+1] = val
        # nums1[:] = sorted(nums1[:m] + nums2)
