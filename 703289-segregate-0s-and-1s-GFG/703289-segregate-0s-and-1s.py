class Solution:
    def segregate0and1(self, arr):
        i=0
        j = len(arr)-1 
        if len(arr) == 0: 
            return None 
        while i < j : 
            if arr[i] == 0: 
                i += 1
            elif arr[j] == 1:
                j -= 1
            else :
                arr[i] , arr[j] = arr[j] , arr[i]
                i += 1
                j -= 1
        
        return arr
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna