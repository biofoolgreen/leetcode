'''
@Description: 
@Version: 
@Author: liguoying@iiotos.com
@Date: 2019-12-19 23:10:07
@LastEditTime: 2019-12-19 23:42:01
@LastEditors: 
'''
# 题目描述
"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:
---
输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
---
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
---
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # lens = len(s)
        # if lens<=1:
        #     return lens
        
        # slow, fast = 0, 0
        # max_sub = 0
        # substring = ""
        # while fast < lens:
        #     if s[fast] in substring:
        #         slow += 1
        #         if slow == fast:
        #             fast += 1
        #     else:
        #         fast += 1
        #     substring = s[slow:fast]
        #     # print(f"slow={slow}, fast={fast}, subs={substring}")
        #     max_sub = max(max_sub, fast-slow)
        # return max_sub
        seen = {}
        left = 0
        max_len = 0
        for i, char in enumerate(s):
            if char in seen:
                left = max(left, seen[char]+1)
            seen[char] = i
            max_len = max(max_len, i-left+1)
            print(f"i={i}, char={char}, left={left}, seen={seen}, maxlen={max_len}")
        return max_len
        
        


if __name__ == "__main__":
    s = Solution()
    str1 = "abcabcbb"
    str2 = "pwwkew"
    str3 = "bbbbbbb"
    print(s.lengthOfLongestSubstring(str2))