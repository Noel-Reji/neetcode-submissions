class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        cnt=0
        for i in range(len(nums)):
            if nums[i] in seen:
                cnt=1
                break
            seen.add(nums[i])
        if cnt==1:
            return(True)
        else:
            return(False)