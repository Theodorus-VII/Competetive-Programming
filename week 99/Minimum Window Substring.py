class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start = 0
        end = -1
        best = ""
        hash_map = {}


        for char in t:
            if char in hash_map:
                hash_map[char] += 1
            else:
                hash_map[char] = 1

        # if s[start] in hash_map:
        #     hash_map[s[start]] -= 1

        while end < len(s):
            end += 1
            if end<len(s):
                if s[end] in hash_map:
                    hash_map[s[end]] -= 1

            flag = True
            for char in hash_map:
                if hash_map[char] > 0:
                    flag = False
                    break

            if flag:
                while start<end:
                    if s[start] in hash_map:
                        hash_map[s[start]] += 1
                        if hash_map[s[start]] > 0:
                            if best == "" or len(best) > end-start:
                                best = s[start:end+1]
                            start += 1
                            break
                    start += 1
                if end<len(s):
                    if s[end] in hash_map:
                        hash_map[s[end]] -= 1
        print(best)
        return best
                

sol=Solution()
s="ab"
t="a"
sol.minWindow(s,t)