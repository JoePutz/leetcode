#python stuff leetcode

class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        # Pointer for the unique element
        k = 1
        
        # Iterate over the array starting from the second element
        for i in range(1, len(nums)):
            # If the current element is different from the previous one, it's unique
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        
        # The array nums now contains the unique elements in the first k positions
        return k

