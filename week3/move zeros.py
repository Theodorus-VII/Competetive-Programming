class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        i=0
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
            else:
                i+=1
        
        for i in range(len(nums), length):
            nums.append(0)