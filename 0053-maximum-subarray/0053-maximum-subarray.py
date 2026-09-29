class Solution(object):
    def maxSubArray(self, nums):
        curr_num = nums[0]
        max_sum = nums[0]
        
        for i in range(1 , len(nums)):
            curr_num = max(nums[i] , curr_num + nums[i])
            max_sum = max(curr_num , max_sum)
        
        return max_sum

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna