class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return self.plusOneI(digits, len(digits) - 1)

    def plusOneI(self, digits: List[int], end_index):
        if digits[end_index] == 9:
            digits[end_index] = 0
            if end_index == 0:
                digits.insert(0, 1)
                return digits
            return self.plusOneI(digits, end_index - 1)

        digits[end_index] += 1

        return digits
