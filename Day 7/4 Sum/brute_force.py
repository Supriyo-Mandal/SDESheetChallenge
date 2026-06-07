class Solution:
    # Function to find quadruplets with sum = target
    def fourSum(self, arr, target):
        # Get size of array
        n = len(arr)
        # Use set to store unique quadruplets
        st = set()

        # First loop - pick first element
        for i in range(n):
            # Second loop - pick second element
            for j in range(i + 1, n):
                # Third loop - pick third element
                for k in range(j + 1, n):
                    # Fourth loop - pick fourth element
                    for l in range(k + 1, n):
                        # If sum equals target
                        if arr[i] + arr[j] + arr[k] + arr[l] == target:
                            # Store sorted quadruplet as tuple
                            temp = tuple(sorted([arr[i], arr[j], arr[k], arr[l]]))
                            st.add(temp)

        # Convert set to list of lists
        return [list(quad) for quad in st]


# Driver code
arr = [1, 0, -1, 0, -2, 2]
target = 0

obj = Solution()
ans = obj.fourSum(arr, target)
print(ans)
