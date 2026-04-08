class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lp, rp = 0, len(numbers) -1 
        while lp < rp:
            pSum = numbers[lp] + numbers[rp]
            if pSum == target:
                return [lp + 1, rp + 1]
            elif pSum < target: 
                lp += 1
            elif pSum > target:
                rp -= 1 