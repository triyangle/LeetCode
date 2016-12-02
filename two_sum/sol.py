class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sorted_nums = sorted(nums)
        low, high = 0, len(nums) - 1
        while low < high:
            if sorted_nums[low] + sorted_nums[high] == target:
                lower, upper = sorted_nums[low], sorted_nums[high]
                break
            elif sorted_nums[low] + sorted_nums[high] > target:
                high -= 1
            else:
                low += 1
        
#        i, lower_index, upper_index = 0, None, None
#        while (lower_index is None or upper_index is None) and i < len(nums):
#            if lower_index is None and nums[i] == lower:
#                lower_index = i
#            elif upper_index is None and nums[i] == upper:
#                upper_index = i
#            i += 1
        for i in range(len(nums)):
            if nums[i] == lower:
                lower_index = i
                break;

        for j in range(len(nums) - 1, -1, -1):
            if nums[j] == upper:
                upper_index = j
                break;
                
        return [min(lower_index, upper_index), max(lower_index, upper_index)]
