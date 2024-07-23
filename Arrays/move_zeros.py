#move zeros to right

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        temp=[]
        for i in range(len(nums)):
            if nums[i]!=0:
                temp.append(nums[i])
        for i in range(len(nums)):
            if i<len(temp):
                nums[i]=temp[i]
            else:
                nums[i]=0