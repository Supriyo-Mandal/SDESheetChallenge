class Solution:
    # Variant 1: Check if two numbers sum to target using two-pointer approach
    def two_sum_exists(self, arr, target):
        # Create list of tuples (value, original_index)
        nums_with_index = [(num, idx) for idx, num in enumerate(arr)]
        
        # Sort list based on the values (to apply two-pointer technique)
        nums_with_index.sort(key=lambda x: x[0])

        # Initialize two pointers: left at start, right at end
        left, right = 0, len(arr) - 1
        
        # Continue until pointers cross
        while left < right:
            # Calculate sum of values at pointers
            current_sum = nums_with_index[left][0] + nums_with_index[right][0]
            
            if current_sum == target:
                # Found a pair
                return "YES"
            elif current_sum < target:
                # Sum too small, move left pointer to right to increase sum
                left += 1
            else:
                # Sum too large, move right pointer to left to decrease sum
                right -= 1
        
        # No pair found
        return "NO"

    # Variant 2: Return indices of two numbers that sum to target
    def two_sum_indices(self, arr, target):
        # Create list of tuples (value, original_index)
        nums_with_index = [(num, idx) for idx, num in enumerate(arr)]
        
        # Sort the list by values
        nums_with_index.sort(key=lambda x: x[0])

        left, right = 0, len(arr) - 1
        
        while left < right:
            current_sum = nums_with_index[left][0] + nums_with_index[right][0]
            if current_sum == target:
                # Return original indices of found elements
                return [nums_with_index[left][1], nums_with_index[right][1]]
            elif current_sum < target:
                # Move left pointer right to increase sum
                left += 1
            else:
                # Move right pointer left to decrease sum
                right -= 1
        
        # No valid pair found
        return [-1, -1]

if __name__ == "__main__":
    sol = Solution()
    arr = [2, 6, 5, 8, 11]
    target = 14

    print(sol.two_sum_exists(arr, target))  # Output: YES
    print(sol.two_sum_indices(arr, target)) # Output: [1, 3]
