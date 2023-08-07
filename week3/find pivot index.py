class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ls = 0
        s = sum(nums)
        for i in range(len(nums)):
            rs = s - nums[i] - ls
            if ls == rs:
                return i
            ls += nums[i]
        return -1

        #15