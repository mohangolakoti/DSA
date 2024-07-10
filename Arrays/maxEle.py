from typing import List
class Solution:
    def largest(self, n : int, arr : List[int]) -> int:
        max=arr[0]
        for i in arr:
            if i>max:
                max=i
        return max
        