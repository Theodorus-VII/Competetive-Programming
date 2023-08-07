class Solution:
    def subarraySum(self, nums, k: int) -> int:
        # subarrs = 0
        # curr = 0
        # arr = [0]
        # for i in range(len(nums)):
        #     curr += nums[i]
        #     # arr.append(curr)
        #     if curr-k in d:
        #         subarrs+=1
        # return subarrs
        # 
        # 
        #too slow
            
        subarrs = 0
        curr = 0

        #prefix sum initialization(at the start it is 0)
        dic = {0:1}
        for i in nums:
            curr += i   #culminative sum
            if curr - k in dic:     #finds subarrs
                subarrs += dic[curr-k]

            if curr not in dic:     #if first occurence of culm sum, create its mapping
                dic[curr] = 1
            else:
                dic[curr]+=1
 
        return subarrs

#7, 25