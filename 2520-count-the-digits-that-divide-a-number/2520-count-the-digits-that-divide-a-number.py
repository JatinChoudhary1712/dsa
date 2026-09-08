class Solution(object):
    def countDigits(self, num):
        count = 0
        n = num

        while n > 0:
            digit = n % 10

            if num % digit == 0:
                count += 1

            n = n // 10

        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna