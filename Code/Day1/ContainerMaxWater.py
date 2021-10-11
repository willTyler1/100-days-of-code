class Solution:
    def maxArea(self, height: List[int]) -> int:
        areaMax = 0;
        for i in range(len(height)): 
            for j in range (i+1, len(height)):
                areaMax = max(areaMax, (j-i) * min(height[i], height[j]))
        return areaMax
