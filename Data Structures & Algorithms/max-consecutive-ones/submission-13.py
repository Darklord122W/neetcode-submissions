class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        big_n=0
        for i in range(0, len(nums)):
            if nums[i]==1:
                n=1
                for j in range(i+1,len(nums)):
                    if nums[j] == 1:
                        n += 1
                    else:
                        if n>big_n:
                            big_n=n
                        break


        return big_n
