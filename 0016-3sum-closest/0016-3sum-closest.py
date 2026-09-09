class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)
        closest = nums[0] + nums[1] + nums[2]
        for i in range(n - 2): 
            j = i+1
            k = n-1 
            while j < k : 
                sum = nums[i] + nums[j] + nums[k]
                if target == sum : 
                    return sum 
                if target != sum:
                    if abs(sum - target) < abs(closest - target):
                        closest = sum
                    if target > sum: 
                        j += 1
                    if target < sum : 
                        k -= 1
        return closest


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna