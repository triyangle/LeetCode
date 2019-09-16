class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_shifted = 0
        base_start_index = 0
        current_index = 0
        replaced_val = nums[0]

        while num_shifted < len(nums):
            shifted_index = (current_index + k) % len(nums)
            temp = nums[shifted_index]
            nums[shifted_index] = replaced_val
            replaced_val = temp
            num_shifted += 1

            if num_shifted == len(nums):
                break

            if shifted_index == base_start_index:
                base_start_index += 1
                current_index = base_start_index
                replaced_val = nums[current_index]
            else:
                current_index = shifted_index
