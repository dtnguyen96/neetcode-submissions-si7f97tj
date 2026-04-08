class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        idx1, idx2 = 0, len(numbers) - 1
        while idx1 < idx2:
            tmpSum = numbers[idx1] + numbers[idx2]
            if tmpSum == target: 
                return [idx1 +1, idx2 +1]
            elif tmpSum > target: 
                idx2 -= 1
            else: 
                idx1 += 1