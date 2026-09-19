class Solution(object):
    def totalFruit(self, fruits):
        left = 0
        freq = {}
        max_fruit = -1

        for right in range(len(fruits)): 
            if fruits[right] in freq:
                freq[fruits[right]] += 1 
            else: 
                freq[fruits[right]] = 1

            while len(freq) > 2:
                freq[fruits[left]] -= 1
                if freq[fruits[left]] == 0:
                    del freq[fruits[left]]
                left += 1
            
            max_fruit = max(max_fruit, right - left + 1)

        return max_fruit

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna