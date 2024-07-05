class Solution: 
    def select(self, arr, i):
        for i in range(len(arr)):
            mini=i
            for j in range(i,len(arr)):
                if arr[mini]>arr[j]:
                    mini=j
            arr[mini], arr[i] = arr[i], arr[mini]
    
    def selectionSort(self, arr,n):
        arr=self.select(arr,n)