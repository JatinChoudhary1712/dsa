class Solution:
    def longestKSubstr(self, s, k):
        # code here
        left = 0 
        max_len = -1
        freq = {}
        
        for right in range(len(s)):
            char = s[right]
            
            if char in freq:
                freq[char] += 1 
            else: 
                freq[char] = 1
                
            while len(freq) > k:
                left_char = s[left]
                freq[left_char] -= 1 
                
                if freq[left_char] == 0:
                    del freq[left_char]
                    
                left += 1
                
            if len(freq) == k:
                max_len = max(max_len, right - left + 1)
                    
        return max_len

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna