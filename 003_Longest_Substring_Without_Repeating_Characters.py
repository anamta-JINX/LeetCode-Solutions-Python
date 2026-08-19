# 3. Longest Substring Without Repeating Characters
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given a string s, find the length of the longest substring without duplicate characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:

# 0 <= s.length <= 105
# s consists of English letters, digits, symbols and spaces.

#SOLUTION:

class Solution(object):
    def lengthOfLongestSubstring(self, s):

        # This set will store the characters
        # currently inside our sliding window.
        #
        # A set is useful because it cannot contain duplicates.
        char_set = set()

        # 'left' represents the starting position
        # of our sliding window.
        left = 0

        # Stores the longest substring length
        # we have found so far.
        max_length = 0

        # 'right' moves through the string
        # one character at a time.
        for right in range(len(s)):

            # If the current character is already inside
            # our window, we have found a duplicate.
            #
            # Keep removing characters from the LEFT
            # until the duplicate disappears.
            while s[right] in char_set:

                # Remove the character at the left
                # side of the window.
                char_set.remove(s[left])

                # Move the left side of the window
                # one position forward.
                left += 1

            # Now s[right] is not a duplicate,
            # so add it to our current window.
            char_set.add(s[right])

            # Calculate the size of the current window.
            #
            # Example:
            #
            # left = 0
            # right = 2
            #
            # indexes: 0, 1, 2
            #
            # therefore length = 3
            #
            # right - left + 1
            current_length = right - left + 1

            # Compare our current window length
            # with the longest length found so far.
            max_length = max(max_length, current_length)

        # After checking the entire string,
        # return the longest length.
        return max_length