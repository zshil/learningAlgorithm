'''
leetcode
26. 删除排序数组中的重复项
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0:return
        i = 0
        for j in range(1,length):
            if nums[i] != nums[j]:
                i +=1
                nums[i] = nums[j]
        return i+1
