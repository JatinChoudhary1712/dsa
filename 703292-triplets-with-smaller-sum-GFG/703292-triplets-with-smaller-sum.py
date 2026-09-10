class Solution:
    def countTriplets(self, sum, arr):
        arr.sort()
        n = len(arr)
        count = 0 

        for i in range(n-2):
            j = i+1 
            k = n-1 

            while j < k:
                curr_sum = arr[i] + arr[j] + arr[k]

                if curr_sum < sum:
                    count += k - j
                    j += 1
            
                else:
                    k -= 1

        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna