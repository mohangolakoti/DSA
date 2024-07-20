#Check if Array Is Sorted and Rotated
class Solution:
    def check(self, nums: List[int]) -> bool:
        c=0
        for i in range(len(nums)):
            if nums[(i+1)%len(nums)]<nums[i]:
                c+=1
            if c>1:
                return False
        return True
