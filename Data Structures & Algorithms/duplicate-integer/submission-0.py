class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        pySet = set()
        for num in nums:
            if num in pySet:
                return True 
            else:
                pySet.add(num)
        return False 
