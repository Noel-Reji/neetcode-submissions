class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        seen=[]
        k=0
        for i in nums:
            if i != val:
                k=k+1
                seen.append(i)
        for i in range(k):
            nums[i]=seen[i]
        return k