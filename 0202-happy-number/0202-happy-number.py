class Solution(object):
    def isHappy(self, n):
         
        def get_fast(num):
            total = 0 

            while num > 0:
                digit = num%10
                total += digit * digit
                num = num//10
            
            return total 

        slow = n 
        fast = get_fast(slow)

        while fast != 1 and slow != fast :
            slow = get_fast(slow)
            fast = get_fast(get_fast(fast))
        
        return fast == 1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna