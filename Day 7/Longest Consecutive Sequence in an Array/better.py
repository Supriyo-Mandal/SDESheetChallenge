
class Solution:
    def longestConsecutive(self, nums):
        n = len(nums)

        # Return 0 if array is empty
        if n == 0:
            return 0 

        nums.sort()

        # Track last smaller element
        lastSmaller = float('-inf') 
        # Count current sequence length
        cnt = 0 
        # Track longest sequence length
        longest = 1 

        for i in range(n):
            # If consecutive number exists
            if nums[i] - 1 == lastSmaller:
                # Increment sequence count
                cnt += 1 
                # Update last smaller element
                lastSmaller = nums[i] 
            # If consecutive number doesn't exist
            elif nums[i] != lastSmaller:
                # Reset count for new sequence
                cnt = 1 
                # Update last smaller element
                lastSmaller = nums[i] 
            # Update longest if needed
            longest = max(longest, cnt) 
        return longest

# Sample array
a = [100, 4, 200, 1, 3, 2]

# Create an instance of solution class
solution = Solution() 
# Function call for finding longest consecutive sequence
ans = solution.longestConsecutive(a) 
print("The longest consecutive sequence is", ans)
