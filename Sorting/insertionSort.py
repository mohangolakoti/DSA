class Solution:
    def insert(self, alist, index):
        current_value = alist[index]
        pos = index
        while pos > 0 and alist[pos - 1] > current_value:
            alist[pos] = alist[pos - 1]
            pos -= 1
        alist[pos] = current_value
    def insertionSort(self, alist, n):
        for i in range(1, n):
            self.insert(alist, i)
        return alist