from typing import List

class Solution:
    # Function to find maximum sum of subarrays
    def maxSubArray(self, nums: List[int]) -> int:
        
        """ Initialize maximum sum with
         the smallest possible integer"""
        maxi = float('-inf')

        # Iterate over each starting index of subarrays
        for i in range(len(nums)):
            
            """ Variable to store the sum
             of the current subarray"""
            sum = 0
            
            """ Iterate over each ending index
             of subarrays starting from i"""
            for j in range(i, len(nums)):
                
                """ Add the current element nums[j] to
                 the sum i.e. sum of nums[i...j-1]"""
                sum += nums[j]

                """ Update maxi with the maximum of its current
                 value and the sum of the current subarray"""
                maxi = max(maxi, sum)

        # Return the maximum subarray sum found
        return maxi

# Main function to test the Solution class
if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    # Create an instance of Solution class
    sol = Solution()

    maxSum = sol.maxSubArray(arr)

    # Print the max subarray sum
    print(f"The maximum subarray sum is: {maxSum}")
