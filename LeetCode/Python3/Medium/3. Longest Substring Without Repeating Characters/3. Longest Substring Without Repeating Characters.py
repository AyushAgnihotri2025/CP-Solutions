class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initialize a dictionary to store the index of each character seen
        char_dict = {}
        # Initialize pointers for the start and end of the substring
        start = 0
        end = 0
        # Initialize a variable to store the length of the longest substring
        max_len = 0
        
        # Loop through each character in the string
        while end < len(s):
            # If the current character has been seen before and is within the current substring
            if s[end] in char_dict and char_dict[s[end]] >= start:
                # Update the start pointer to the next character after the previous occurrence of the current character
                start = char_dict[s[end]] + 1
            # Update the index of the current character in the dictionary
            char_dict[s[end]] = end
            # Update the end pointer to the next character
            end += 1
            # Update the length of the longest substring seen so far
            max_len = max(max_len, end - start)
        
        # Return the length of the longest substring
        return max_len