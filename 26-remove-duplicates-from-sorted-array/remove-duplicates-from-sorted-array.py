class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        output = []
        for i in nums:
            if i in output:
                pass
            else:
                output.append(i)
        nums[:] = output
        return len(nums)