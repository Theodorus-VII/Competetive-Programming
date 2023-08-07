class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # maxlen = 0
        
        # i = 0
        # j = 1
        
        # while j < len(s):
        #     for k in range(i, j):
        #         if s[j] == s[k]:
        #             if j-i > maxlen:
        #                 maxlen = j - i
        #             i = k+1
        #             continue
        #     j+=1
        # if j-i > maxlen:
        #     maxlen = j - i
        # if len(s) == 0:
        #     maxlen = 0
        # return maxlen

        maxlen = 0
        
        i = 0
        j = 0
        dct = {}
        
        while j < len(s):
            if s[j] in dct:
                if j-i > maxlen:
                    maxlen = j - i
                if i < dct[s[j]] + 1:
                    i = dct[s[j]] + 1
                dct[s[j]] = j
                j += 1
                continue

            dct[s[j]] = j  
            j+=1


        if j-i > maxlen:
            maxlen = j - i
        if len(s) == 0:
            maxlen = 0
        return maxlen
            
#5 20