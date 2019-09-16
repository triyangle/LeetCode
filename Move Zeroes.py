class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_zeros = 0

        for num in nums:
            if num == 0:
                num_zeros += 1

        current_index = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[current_index] = nums[i]
                current_index += 1

        for i in range(len(nums) - 1, len(nums) - 1 - num_zeros, -1):
            nums[i] = 0
