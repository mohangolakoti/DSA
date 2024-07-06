class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr, n):
        for i in range(0,n-1):
            for j in range(1,n-i):
                if arr[j-1]>arr[j]:
                    arr[j-1],arr[j] = arr[j],arr[j-1]
        return arr