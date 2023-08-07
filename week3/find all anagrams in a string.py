class Solution:
    def findAnagrams(self, s: str, p: str):
        window = len(p)
        d ={}
        ans = []

        if len(p) > len(s):
            return ans
        for i in p:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        for i in range(window):
            if s[i] in d:
                d[s[i]] -= 1
        
        a=0
        for i in d:
            if d[i] != 0:
                a=-1
        if a!=-1:
            ans.append(0)


        for i in range(1, len(s)-window+1):
            if s[i-1] in d:
                d[s[i-1]] += 1

            end = i + window - 1    #exclusive

            if s[end] in d:
                d[s[end]] -= 1
            else:
                continue
            
            a=0
            for l in d:
                if d[l] != 0:
                    a=-1
                    break
            if a!=-1:
                ans.append(i)
        return ans
            
#2 20