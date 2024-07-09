class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        if low<high:
            mid = self.partition(arr,low,high)
            self.quickSort(arr,low,mid-1)
            self.quickSort(arr,mid+1,high)
    
    def partition(self,arr,low,high):
        pivot = arr[low]
        i=low+1
        j=high
        while i<j:
            while arr[i]<=pivot and i<=j:
                i+=1
            while arr[j]>pivot and j>=i:
                j-=1
            if i<j:
                arr[i],arr[j] = arr[j],arr[i]
        arr[low],arr[j] = arr[j],arr[low]
        return j
