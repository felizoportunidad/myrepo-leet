class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
            
        N = len(nums)
        i = N-1
        j = N-1
        
        while i > 0 and nums[i-1]>=nums[i]:
            i -= 1
            
        if i == 0:
            return nums.reverse()
        
        k = i-1
        while nums[j] <= nums[k]:
            j -= 1
            
        nums[j], nums[k] = nums[k], nums[j]
        
        l,r = k+1, N-1
        
        while l < r:
            
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
            
        return nums
        