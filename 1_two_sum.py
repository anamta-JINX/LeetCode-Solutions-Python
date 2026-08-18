# You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
 

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

nums = [2,7,11,15]
target = 9

class Solution(object):
    def twoSum(self, nums, target):

        seen = {}

        for i in range(len(nums)):

            current_num = nums[i]

            needed = target - current_num

            if needed in seen:
                return [seen[needed], i]

            seen[current_num] = i

#Calling the function and printing it 
solution = Solution()
print(solution.twoSum(nums, target))
            
#             explanation:
# Create an empty dictionary called seen.

# For every index in nums:

#     Get the current number.

#     Calculate the number needed.

#     If that needed number was already seen:
#         return its old index and my current index.

#     Otherwise:
#         remember the current number and its index.