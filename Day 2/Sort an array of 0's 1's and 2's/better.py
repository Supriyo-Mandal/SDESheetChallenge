class Solution:
    # Function to sort an array containing only 0s, 1s, and 2s
    def sortZeroOneTwo(self, nums):
        # Count of 0s, 1s, and 2s
        cnt0 = cnt1 = cnt2 = 0

        # First pass: Count the number of 0s, 1s, and 2s
        for num in nums:
            if num == 0:
                cnt0 += 1
            elif num == 1:
                cnt1 += 1
            else:
                cnt2 += 1

        # Second pass: Fill the array with 0s, then 1s, then 2s

        # Fill first 'cnt0' elements with 0
        for i in range(cnt0):
            nums[i] = 0

        # Fill next 'cnt1' elements with 1
        for i in range(cnt0, cnt0 + cnt1):
            nums[i] = 1

        # Fill remaining elements with 2
        for i in range(cnt0 + cnt1, len(nums)):
            nums[i] = 2

# Driver code
nums = [0, 2, 1, 2, 0, 1]
sol = Solution()
sol.sortZeroOneTwo(nums)
print("After sorting:")
print(nums)
