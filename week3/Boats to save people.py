class Solution:
    def numRescueBoats(self, people, limit: int) -> int:
        #max sum below the limit
        #need indexes
        #also need to keep track of what ive added
        #counter for boats. but kinda unecessary

        people.sort()
        i = 0 
        j = len(people) - 1
        boats = 0

        while i < j:
            if people[i] + people[j] <= limit:
                boats += 1
                i += 1
                j -= 1
            else:
                j -= 1
                boats += 1
        

        return boats
        # 7

x = Solution()
people = [3,5,3,4]
limit = 5
x.numRescueBoats(people, limit)