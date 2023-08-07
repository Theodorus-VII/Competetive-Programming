class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        d = {}

        i = 0
        j = 0

        while j < len(fruits):
            if fruits[j] in d:
                d[fruits[j]] += 1
            else:
                d[fruits[j]] = 1

            if len(d) > 2:
                d[fruits[i]] -= 1
            
                if d[fruits[i]] == 0:
                    del d[fruits[i]]
                i += 1
            j+=1
        return j-i
                

            
# 1 15