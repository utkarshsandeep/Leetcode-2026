class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        j=0
        output = []
        for i in range(len(nums)):
            flag=False
            for j in range(len(nums)):
                if i==j:
                    continue
                if nums[i]+nums[j]==target:
                    flag=True
                    break
            if flag:
                break
        output.append(i)
        output.append(j)
        return output