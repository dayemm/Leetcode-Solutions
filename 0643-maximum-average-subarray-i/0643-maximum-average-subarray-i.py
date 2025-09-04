class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Brute Force Approach check all pairs:O(nxk)complexity
        # 96/127 test cases passed
        # maxsum=float('-inf')
        # currentsum=0

        # for a in range(len(nums)-k+1):
            
        #     for b in range(a,a+k):
        #         currentsum+=nums[b]
        #     maxsum=max(maxsum,currentsum)
        #     currentsum=0
        # return maxsum/k

        #Optimized 0(n) Sliding wali window:
        maxsum=0
        currentsum=0
        for a in range(k):
            currentsum+=nums[a]
        maxsum=currentsum

        for b in range(k,len(nums)):
            currentsum-=nums[b-k]
            currentsum+=nums[b]
            maxsum=max(currentsum,maxsum)
        return maxsum/k


        
      
        



        