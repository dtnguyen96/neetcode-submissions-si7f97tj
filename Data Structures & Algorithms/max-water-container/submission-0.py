class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0 
        r = len(heights) - 1
        maxArea = 0
        while l < r: 
            if heights[r] > heights[l]:
                area = (r-l) * heights[l]
                l+=1
            else:
                area = (r-l) * heights[r]
                r-=1
            maxArea = max(area, maxArea)
        return maxArea