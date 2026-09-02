class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)

        if not n:
            return 0

        i = 0
        j = i + 1

        while j < n:
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]

            j += 1

        return i + 1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna