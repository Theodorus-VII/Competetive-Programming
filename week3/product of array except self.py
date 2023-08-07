class Solution:
    def productExceptSelf(self, nums) :
        a = [1] * (len(nums))
        ls = 1
        rs = 1

        for i in range(len(nums)):
            a[i] *= ls
            ls *= nums[i]

            a[len(nums) - 1 - i] *= rs
            rs *= nums[len(nums) - i - 1]
        return a


# 15 2
x = Solution()
nums = [1,2,3,4]
x.productExceptSelf(nums)