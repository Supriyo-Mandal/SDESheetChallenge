class Solution:
    # Variant 1: Check if two numbers sum to target using hashing
    def two_sum_exists(self, arr, target):
        mp = {}  # Dictionary to store element -> index
        # Iterate over all elements
        for i, num in enumerate(arr):
            complement = target - num
            # Check if complement exists in dictionary
            if complement in mp:
                return "YES"  # Pair found
            # Store current element and its index
            mp[num] = i
        # No pair found
        return "NO"

    # Variant 2: Return indices of two numbers that sum to target using hashing
    def two_sum_indices(self, arr, target):
        mp = {}  # Dictionary to store element -> index
        for i, num in enumerate(arr):
            complement = target - num
            # If complement found, return indices
            if complement in mp:
                return [mp[complement], i]
            # Store current element and index
            mp[num] = i
        # No pair found
        return [-1, -1]

if __name__ == "__main__":
    sol = Solution()
    arr = [2, 6, 5, 8, 11]
    target = 14

    print(sol.two_sum_exists(arr, target))
    print(sol.two_sum_indices(arr, target))
