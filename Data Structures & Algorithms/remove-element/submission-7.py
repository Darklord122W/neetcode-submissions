class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=0
        for i, Element in enumerate(nums):
            if Element!=val:
                k+=1
            else:  # the same value scenario, we can make that position the next following not same value and make that position '_'
            # if in boundary
                # if (i+1) == len(nums):
                #     # directly change that position to '_'
                #     nums[i]='_'
                # else:
                for j in range(i+1,len(nums)):
                    nums[j - 1] = nums[j]
                    nums[len(nums)-1]='_'
        
        return k
