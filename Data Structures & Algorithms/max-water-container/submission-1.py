class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r=0,len(heights)-1
        totarea=0
        while l<r:
            width=r-l
            length=min(heights[l],heights[r])
            area=length*width
            totarea=max(totarea,area)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return totarea
