"""
Given a list of integers determine if it can be partitioned into two equal list

Example input: [1,5,11,5]
Example output: True
Explanation: list can be partitioned into [1,5,5] and [11] which both sum up to 11
"""

# ChatGPT
def can_partition(nums):
    # Calculate the sum of all elements in the list
    total_sum = sum(nums)
    # If the sum is odd, return False
    if total_sum % 2 != 0:
        return False
    # Divide the sum by 2 to get the target sum of each partition
    target_sum = total_sum // 2
    # Create a boolean 2D array to store whether a partition can be formed with the given sum
    dp = [[False for _ in range(target_sum + 1)] for _ in range(len(nums) + 1)]
    # Initialize the first row of the array to True
    for i in range(len(dp)):
        dp[i][0] = True
    # Iterate over the rows and columns of the array
    for i in range(1, len(dp)):
        for j in range(1, target_sum + 1):
            # If the current element can be included in a partition that adds up to the current sum
            if nums[i - 1] <= j:
                # Set the value of the current element based on whether a partition can be formed
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
            else:
                # If the current element cannot be included in a partition that adds up to the current sum, copy the value from the previous row
                dp[i][j] = dp[i - 1][j]
    # Return the value in the bottom-right corner of the array
    return dp[-1][-1]


print(can_partition([0, 1, 1]))
