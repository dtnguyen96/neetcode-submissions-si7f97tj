
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevValues = {}
        for i, v in enumerate(nums): 
            if target - v in prevValues:
                return [prevValues[target-v], i]
            prevValues[v] = i
        return 


        