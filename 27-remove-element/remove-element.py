class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        output = []
        for i in nums:
            if i == val:
                pass
            else:
                output.append(i)
        nums[:]=output
        return len(nums)