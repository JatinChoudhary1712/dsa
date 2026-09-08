class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 2):

            # Skip duplicate first elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = n - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total == 0:
                    result.append([nums[i], nums[j], nums[k]])

                    j += 1
                    k -= 1

                    # Skip duplicate j
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    # Skip duplicate k
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

                elif total > 0:
                    k -= 1

                else:
                    j += 1

        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna