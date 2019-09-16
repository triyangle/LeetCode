class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
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

    def twoSumMap(self, nums: List[int], target: int) -> List[int]:
        num_dict = dict()

        for i, num in enumerate(nums):
            if num not in num_dict:
                num_dict[num] = [i]
            else:
                num_dict[num].append(i)

        for i, num in enumerate(nums):
            diff = target - num

            if diff in num_dict:
                if diff == num and len(num_dict[diff]) == 1:
                    continue
                else:
                    return [i, num_dict[diff][0]]
