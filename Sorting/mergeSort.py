class Solution:
    def merge(self,arr, l, m, r): 
        left=l
        right=m+1
        temp=[]
        while left<=m and right<=r:
            if arr[left]<=arr[right]:
                temp.append(arr[left])
                left+=1
            else:
                temp.append(arr[right])
                right+=1
        while left<=m:
            temp.append(arr[left])
            left+=1
        while right<=r:
            temp.append(arr[right])
            right+=1
            
        for i in range(len(temp)):
            arr[l + i] = temp[i]

    def mergeSort(self,arr, l, r):
        if l>=r:
            return
        m=(l+r)//2
        self.mergeSort(arr,l,m)
        self.mergeSort(arr,m+1,r)
        self.merge(arr,l,m,r)
