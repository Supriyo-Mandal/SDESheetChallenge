
class Solution:
    # Helper function to perform linear search
    def linearSearch(self, nums, num):
        n = len(nums)
        # Traverse through the array
        for i in range(n):
            if nums[i] == num:
                return True
        return False

    def longestConsecutive(self, nums):
        # If the array is empty
        if len(nums) == 0:
            return 0
        n = len(nums)
        # Initialize the longest sequence length
        longest = 1

        # Iterate through each element in the array
        for i in range(n):
            # Current element
            x = nums[i]
            # Count of the current sequence
            cnt = 1

            # Search for consecutive numbers
            while self.linearSearch(nums, x + 1):
                # Move to the next number in the sequence
                x += 1
                # Increment the count of the sequence
                cnt += 1

            # Update the longest sequence length found so far
            longest = max(longest, cnt)
        return longest

if __name__ == "__main__":
    a = [100, 4, 200, 1, 3, 2]

    # Create an instance of the Solution class
    solution = Solution()

    # Function call for longest consecutive sequence
    ans = solution.longestConsecutive(a)
    print("The longest consecutive sequence is", ans)
