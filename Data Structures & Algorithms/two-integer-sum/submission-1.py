
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevValues = {}
        for i, v in enumerate(nums): 
            diff = target - v
            if diff in prevValues:
                return [prevValues[diff], i]
            prevValues[v] = i
        return 


        