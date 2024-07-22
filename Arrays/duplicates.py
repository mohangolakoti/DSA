#Remove duplicates from sorted array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        unique_nums = []
        seen = set()

        for num in nums:
            if num not in seen:
                unique_nums.append(num)
                seen.add(num)
        
        for i in range(len(unique_nums)):
            nums[i] = unique_nums[i]
        
        return len(unique_nums)
