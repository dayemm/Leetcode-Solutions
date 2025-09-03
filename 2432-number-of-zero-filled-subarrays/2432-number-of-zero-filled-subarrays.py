class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        total_subarrays=0
        zero_count=0
        for number in  nums:
            if number==0:
                zero_count=zero_count+1
                total_subarrays+=zero_count
            else:
                zero_count=0
        return total_subarrays
        