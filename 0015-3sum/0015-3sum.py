class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #(O(n^3)) compelxity Brute force passed 309/314 test cases
        # returnarr=[]
        # for a in range(len(nums)):
        #     for b in range(a+1,len(nums)):
        #         for c in range(b+1,len(nums)):
        #             if nums[a]+nums[b]+nums[c]==0:
        #                 returnarr.append([nums[a],nums[b],nums[c]])
        # return  list(map(list, {tuple(sorted(row)) for row in returnarr}))

        #Optimized O(n^2) reduction to 2 sum approach
        nums.sort()
        return_arr=[]

        for a in range(len(nums)):
            if a>0 and nums[a]==nums[a-1]:
                continue
            leftptr=a+1
            rightptr=len(nums)-1
            while leftptr < rightptr:
                if nums[a]+nums[leftptr]+nums[rightptr]<0:
                    leftptr+=1
                elif nums[a]+nums[leftptr]+nums[rightptr]>0:
                    rightptr-=1
                else:
                    return_arr.append([nums[a],nums[leftptr],nums[rightptr]])
                    while  leftptr < rightptr and nums[leftptr]==nums[leftptr+1]:
                        leftptr+=1
                    while leftptr < rightptr and nums[rightptr]==nums[rightptr-1]:
                        rightptr -=1
                    leftptr+=1
                    rightptr-=1
        return  return_arr




        