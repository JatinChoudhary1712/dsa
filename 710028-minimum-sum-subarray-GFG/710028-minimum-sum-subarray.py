class Solution:
    def minSubarraySum(self, arr: list[int]) -> int:
        # code here
        curr_num = arr[0]
        min_sum = arr[0]
        
        for i in range(1 , len(arr)):
            curr_num = min(arr[i] , curr_num + arr[i])
            min_sum = min(curr_num , min_sum)
        
        return min_sum

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna