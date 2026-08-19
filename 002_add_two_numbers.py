# 2. Add Two Numbers
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

# Example 2:
# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
 

# Constraints:

# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next




l1 = [2,4,3]
l2 = [5,6,4]
class Solution(object):
    def addTwoNumbers(self, l1, l2):

        # Dummy node makes it easier to build the result linked list.
        # This node itself will not be part of the final answer.
        dummy = ListNode(0)

        # 'current' points to the last node in the result list.
        current = dummy

        # Carry from the previous addition.
        carry = 0

        # Continue while either linked list still has nodes
        # or there is still a carry left.
        while l1 or l2 or carry:

            # Get the current value from l1.
            # If l1 is finished, use 0.
            val1 = l1.val if l1 else 0

            # Get the current value from l2.
            # If l2 is finished, use 0.
            val2 = l2.val if l2 else 0

            # Add both digits and the previous carry.
            total = val1 + val2 + carry

            # Get the new carry.
            # Example: 14 // 10 = 1
            carry = total // 10

            # Get the digit that should go into the current result node.
            # Example: 14 % 10 = 4
            digit = total % 10

            # Create a new node containing the result digit.
            current.next = ListNode(digit)

            # Move current to the new node.
            current = current.next

            # Move l1 to its next node if it exists.
            if l1:
                l1 = l1.next

            # Move l2 to its next node if it exists.
            if l2:
                l2 = l2.next

        # Skip the dummy node and return the real result.
        return dummy.next