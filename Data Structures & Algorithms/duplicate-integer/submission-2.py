class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        cnt=0
        for i in nums:
            if i in seen:
                cnt=1
                break
            seen.add(i)
        if cnt==1:
            return(True)
        else:
            return(False)