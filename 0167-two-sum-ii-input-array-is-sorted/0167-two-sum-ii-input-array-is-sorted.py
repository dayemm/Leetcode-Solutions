class Solution:
       def twoSum(self, nums: List[int], target: int) -> List[int]:
        leftptr=0
        rightptr=len(nums)-1

        while leftptr != rightptr:
           if nums[leftptr]+nums[rightptr]< target:
             leftptr=leftptr+1
           elif  nums[leftptr]+nums[rightptr]> target:
             rightptr=rightptr-1
           elif nums[leftptr]+nums[rightptr]== target:
                return[leftptr+1,rightptr+1]
        return[]
             
        
        