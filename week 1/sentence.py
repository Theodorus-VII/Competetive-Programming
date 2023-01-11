class Solution:
    def sortSentence(self, s: str) -> str:
        sorted_sentence = ''
        for index in range(1, len(s)):
            index_prev = 0
            for i in range(len(s)):
                if (s[i] == " ") or (i == len(s)-1):
                    if(int(s[i-1]) == index):
                        sorted_sentence += s[index_prev: i-1] + " "
                    index_prev = i + 1
        return sorted_sentence
        
x = Solution()
s="is2 sentence4 This1 a3"
print(x.sortSentence(s))