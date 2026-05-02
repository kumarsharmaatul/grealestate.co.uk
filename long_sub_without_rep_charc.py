'''
2. Longest Substring Without Repeating Characters
Problem:
Given a string, return the length of the longest substring without repeating characters. For example:
Input: "abcabcbb"
Output: 3


Solution:
I used the sliding window technique. 
We maintain a window using two pointers (left and right) and a hash map to store the last seen index of each character.
If we encounter a character that is already in our map and is within our current window,
we move the left pointer just past the previous occurrence of that character.
'''


def lengthOfLongestSubstring(s):
    char_map = {}
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        # If character is already in the map and falls within our current window
        if s[right] in char_map and char_map[s[right]] >= left:
            left = char_map[s[right]] + 1
            
        char_map[s[right]] = right
        max_length = max(max_length, right - left + 1)
        
    return max_length

# Test
print(lengthOfLongestSubstring("abcabcbb"))