class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        start = 0
        end = len(s1) -1

        counter = {}
        for char in s1:
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1

        for i in range(end):
            if s2[i] in counter:
                counter[s2[i]] -= 1
        
        while end<len(s2):
            if s2[end] in counter:
                counter[s2[end]] -= 1
                flag = True
                for char in counter:
                    if counter[char] != 0:
                        flag = False
                        break
                        
                if flag: return True
            if s2[start] in counter:
                counter[s2[start]] += 1
            start += 1
            end += 1
        return False
    
s = Solution()
s1="ab"
s2="eidbaooo"
s.checkInclusion(s1,s2)
            
