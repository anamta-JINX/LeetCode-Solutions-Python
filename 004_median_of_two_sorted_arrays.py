# 4. Median of Two Sorted Arrays
# Solved
# Hard
# Topics
# premium lock icon
# Companies
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).


# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


# Constraints:

# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106

#SOLUTION:

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):

        # Always perform binary search on the smaller array.
        # This makes the solution more efficient.
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        # Store the lengths of both arrays.
        m, n = len(nums1), len(nums2)

        # These variables represent the search range
        # for the partition position in nums1.
        left, right = 0, m

        # Keep performing binary search until
        # we find the correct partition.
        while left <= right:

            # Find the partition position in nums1.
            i = (left + right) // 2

            # Calculate the partition position in nums2.
            #
            # Together, both left partitions should contain
            # half of the total elements.
            j = (m + n + 1) // 2 - i

            # Find the values directly to the left and right
            # of the partition in nums1.
            #
            # Use negative infinity if there is nothing on the left.
            # Use positive infinity if there is nothing on the right.
            left1 = float("-inf") if i == 0 else nums1[i - 1]
            right1 = float("inf") if i == m else nums1[i]

            # Find the values directly to the left and right
            # of the partition in nums2.
            left2 = float("-inf") if j == 0 else nums2[j - 1]
            right2 = float("inf") if j == n else nums2[j]

            # A correct partition means that every value
            # on the left side is smaller than or equal to
            # every value on the right side.
            if left1 <= right2 and left2 <= right1:

                # If the total number of elements is odd,
                # the median is the largest value on the left.
                if (m + n) % 2 == 1:
                    return float(max(left1, left2))

                # If the total number of elements is even,
                # the median is the average of the largest
                # value on the left and smallest value on the right.
                return (max(left1, left2) + min(right1, right2)) / 2.0

            # If the left value of nums1 is too large,
            # move the partition towards the left.
            elif left1 > right2:
                right = i - 1

            # Otherwise, move the partition towards the right.
            else:
                left = i + 1