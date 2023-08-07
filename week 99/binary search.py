class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start = 0
        end = len(nums)

        while start<end:
            s = (end+start)//2
            if nums[s] > target:
                end = s
            if nums[s] < target:
                start = s
            if nums[s] == target:
                return s
            
        return -1
    
s = Solution()
print(s.search([-1,0,3,5,9,12], target = 9))