# 394. Decode String
# https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        repeat_num = 0
        cur_string_arr = []
        for char in s:
            if char == '[':
                stack.append(''.join(cur_string_arr))
                stack.append(repeat_num)
                repeat_num = 0
                cur_string_arr = []
            elif char == ']':
                multiplier, prev_string = stack.pop(), stack.pop()
                cur_string = ''.join(cur_string_arr)
                cur_string = prev_string + multiplier*cur_string 
                cur_string_arr = [cur_string]
            elif char.isdigit():
                repeat_num = repeat_num*10 + int(char)
            else:
                cur_string_arr.append(char)
        return ''.join(cur_string_arr)
