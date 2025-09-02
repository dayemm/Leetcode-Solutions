class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Brute FORCE sol O(n^2)
        # maxarea=0

        # for o in range(len(height)):
        #     for i in range(o+1,len(height)):
        #         area= min(height[o],height[i])*(i-o)
        #         if area>maxarea:
        #             maxarea=area
        # return maxarea
        
        #Optimized solution: O(n)
        max_area=0
        left_ptr =0
        right_ptr=len(height)-1

        while left_ptr != right_ptr:
            area=min(height[left_ptr],height[right_ptr])*(right_ptr-left_ptr)
            max_area=max(area,max_area)
            if height[left_ptr]<height[right_ptr]:
                left_ptr +=1
            else:
                right_ptr -=1
        return max_area
            
