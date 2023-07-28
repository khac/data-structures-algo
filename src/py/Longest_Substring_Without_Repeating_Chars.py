# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s:str) -> int:
        repeat_char = defaultdict(int)
        longest_substr_len = 0
        left_index = 0
        for right_index in range(len(s)):
            ordinal_index = ord(s[right_index]) - ord('a')
            repeat_char[ordinal_index] += 1
            while repeat_char[ordinal_index] > 1:
                cur_left_index = ord(s[left_index]) - ord('a')
                repeat_char[cur_left_index] -= 1
                left_index += 1
            longest_substr_len = max(longest_substr_len, right_index-left_index+1)
        return longest_substr_len
