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

# convert roman numerals to arabic numerals
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0

        rom_to_ara = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        for i in range(len(s)):
            if i < len(s)-1 and rom_to_ara[s[i]] < rom_to_ara[s[i + 1]]:
                total -= rom_to_ara[s[i]]
            else:
                total += rom_to_ara[s[i]]
        return total