class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        while k>0:
            temp=nums[n-1]
            for i in range(len(nums)-1,0,-1):
                nums[i] = nums[i-1]
            nums[0] = temp
            k-=1


from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n  # Correctly adjust k to be within the bounds of the array length

        # Create a new array to hold the rotated elements
        rotated = [0] * n

        for i in range(n):
            rotated[(i + k) % n] = nums[i]

        # Copy the rotated elements back to the original array
        for i in range(n):
            nums[i] = rotated[i]