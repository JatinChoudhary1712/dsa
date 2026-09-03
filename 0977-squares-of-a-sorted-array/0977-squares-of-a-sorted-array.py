class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        negative = [x for x in nums if x < 0]
        positive = [x for x in nums if x >= 0]

        arr = []

        i = len(negative) - 1
        j = 0

        while i >= 0 and j < len(positive):
            if negative[i] ** 2 > positive[j] ** 2:
                arr.append(positive[j] ** 2)
                j += 1
            else:
                arr.append(negative[i] ** 2)
                i -= 1

        while i >= 0:
            arr.append(negative[i] ** 2)
            i -= 1

        while j < len(positive):
            arr.append(positive[j] ** 2)
            j += 1

        return arr

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna