class Solution:
    def trap(self, height: list[int]) -> int:
        start = 0
        end = 1
        i = 1
        water = 0
        b = 0
        o = 0
        while start < len(height) and end < len(height):
            if i < len(height) - 1:
                b+=height[i]

            if height[i] >= height[end]:
                end = i
                o = b

            if (i == len(height) - 1) or (height[start] <= height[end]):
                h = min(height[start], height[end])
                # for j in range(start, end):
                #     if h > height[j]:
                #         water += h - height[j]
                water += h*(end-(start+1)) - o
                start = end
                b = 0
                i = start
                end += 1
            i+=1

        print(water)
        return water



s = Solution()
n2 = [5,4,1,2]
n3 = [4,2,0,3,2,5]
n = [0,1,0,2,1,0,1,3,2,1,2,1]
s.trap(n)