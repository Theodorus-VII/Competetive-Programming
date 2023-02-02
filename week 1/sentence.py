class Solution:
    def sortSentence(self, s: str) -> str:
        sorted_sentence = ''
        for index in range(1, len(s)):
            index_prev = 0
            for i in range(len(s)):
                if (s[i] == " "):
                    if(int(s[i-1]) == index):
                        if(index==1):
                            sorted_sentence += s[index_prev: i-1]
                        else:
                            sorted_sentence += " " + s[index_prev: i-1]
                    index_prev = i + 1
                if((i==len(s)-1) and int(s[i])==index):
                    if(index==1):
                        sorted_sentence += s[index_prev: i]
                    else:
                        sorted_sentence += " " + s[index_prev: i]
                    index_prev = i + 1

        return sorted_sentence
