class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        current = float('-inf')
        longest_sequence = 0
        current_sequence = 0
        sorted_nums = sorted(nums)
        for num in sorted_nums:
            if (num == current + 1):
                current = num
                current_sequence += 1
            else:
                longest_sequence = max(current_sequence, longest_sequence)
                current_sequence = 1
                current = num
        print(longest_sequence)
        return longest_sequence
    
s = Solution()
s.longestConsecutive(nums = [1,2,0,1])
