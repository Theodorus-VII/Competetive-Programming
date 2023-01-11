class Solution: 
    def select(self, arr, i):
        # code here
        ind = i
        for j in range(i+1, len(arr)):
            if arr[ind] > arr[j]:
                ind = j
        return ind
        
            
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            ind = self.select(arr, i)
            arr[i], arr[ind] = arr[ind], arr[i]
        return arr
