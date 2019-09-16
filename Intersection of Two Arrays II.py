class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2_copy = nums2[:]
        intersection = []

        for num in nums1:
            for num2 in nums2_copy:
                if num == num2:
                    intersection.append(num)
                    nums2_copy.remove(num2)
                    break

        return intersection
