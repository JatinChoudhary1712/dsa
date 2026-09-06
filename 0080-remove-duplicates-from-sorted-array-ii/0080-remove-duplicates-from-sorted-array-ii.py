class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        read = 2
        write = 2

        while read < len(nums):

            if nums[read] == nums[write - 2]:
                # duplicate hai → sirf read aage
                read += 1

            else:
                # valid element hai
                nums[write] = nums[read]
                write += 1
                read += 1

        return write

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna