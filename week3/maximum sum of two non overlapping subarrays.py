class Solution:
    def maxSumTwoNoOverlap(self, nums, firstLen: int, secondLen: int) -> int:

        a = []
        culm = 0
        
        for i in nums:
            culm += i
            a.append(culm)


        suml = a[0]
        sumr = a[firstLen]
        res = a[firstLen-1]

        for i in range(firstLen + secondLen, len(a)):
            ls = i - secondLen
            rs = i - firstLen

            suml = max(suml, a[ls]-a[ls-firstLen])
            sumr = max(sumr, a[rs] - a[rs - secondLen])

            res = max(sumr + a[i] - a[i-firstLen],suml + a[i] - a[i-secondLen], res)
            
        return res

        # s2 = a[0]
        # s1 = a[secondLen]

        # for i in range(len(a)-firstLen):        #secondLen to the left
        #     si = i+secondLen-1
        #     if a[i] > s2:
        #         s2 = a[i]
        #     if a[si] > s1:
        #         s1 = a[si]

        # return max(sum1 + sum2, s1 + s2)
            

x = Solution()
nums =[0,6,5,2,2,5,1,9,4]
firstLen =1
secondLen =2
print(x.maxSumTwoNoOverlap(nums, firstLen, secondLen))