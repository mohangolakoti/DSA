class Solution:
    def print2largest(self, arr):
        max=arr[0]
        for i in arr:
            if i>max:
                max=i
        sl=-1
        for i in arr:
            if i<max and i>sl:
                sl=i
        return sl