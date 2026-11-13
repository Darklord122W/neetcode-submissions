class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n=0
        for i in range(1,len(nums)-1):
            if nums[i-1]==1 and nums[i]==1:
                n+=1
        
        return n