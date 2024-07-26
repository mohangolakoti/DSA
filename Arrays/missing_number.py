class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        n=len(nums)
        if n>1:
            for i in range(1,n):
                if nums[i-1]+1 !=nums[i]:
                    return nums[i]-1
        if nums[0] < 1:
            return max(nums)+1
        else:
            return min(nums)-1
        