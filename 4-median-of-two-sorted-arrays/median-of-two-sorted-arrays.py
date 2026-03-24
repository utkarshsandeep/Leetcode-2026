class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1+nums2


        sortedNums = sorted(nums)
        print(sortedNums)
        mid = len(nums)//2
        if len(sortedNums)%2 == 0:
            return ((sortedNums[mid-1] + sortedNums[mid])/2)
        else:
            return (sortedNums[mid])