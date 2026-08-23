class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        streak=0
        nstreak=0
        for i in nums:
            if i==1:
                nstreak+=1
            else:
                nstreak=0
            streak=max(streak,nstreak)
        return streak