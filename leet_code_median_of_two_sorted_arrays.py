class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x = sorted(nums1 + nums2)
        n = len(x)
        if (n % 2) != 0:
            return x[(n//2)]
        else:
            return (x[(n//2)-1] + x[(n//2)]) / 2
            
