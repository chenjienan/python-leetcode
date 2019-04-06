# LintCode 1639 K-Substring with K different characters

# Given a string S and an integer K.
# Calculate the number of substrings of length K and containing K different characters

# Have you met this question in a real interview?  
# Example
# Example 1:

# Input："abcabc"，k=3
# Output：3
# Explanation：
# substrings:  ["abc", "bca", "cab"]
# Example 2:

# Input："abacab"，k=3
# Output：2
# Explanation：
# substrings: ["bac", "cab"]

class Solution:
    """
    @param stringIn: The original string.
    @param K: The length of substrings.
    @return: return the count of substring of length K and exactly K distinct characters.
    """
    def KSubstring(self, stringIn, K):
        # Write your code here
        if len(stringIn) < K: return 0

        dist_substring = set()
        window = ''
        
        for c in stringIn:
            if c in window:
                window = window[window.index(c) + 1:]
                
            window += c
            
            if len(window) == K:
                dist_substring.add(window)
                window = window[1:]
        
        return len(dist_substring)

    # def KSubstring(self, stringIn, K):
    #     # Write your code here
    #     char = ""
    #     s = set()
    #     for c in stringIn:
    #         if len(char) == K:
    #             s.add(char)
    #             char = char[1:]
    #         if c in char:
    #             index = char.find(c)
    #             char = char[index+1:]
    #         char += c
    #     if len(char) == K:
    #         s.add(char)
    #     return len(s)