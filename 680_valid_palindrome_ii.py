"""
给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。

示例 1:

输入: "aba"
输出: True
示例 2:

输入: "abca"
输出: True
解释: 你可以删除c字符。
注意:

字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-palindrome-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) <= 2:
            return True

        def checkPalindrome(low, high):
            i, j = low, high
            while i<j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        left = 0
        right = len(s)-1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return checkPalindrome(left+1, right) or checkPalindrome(left, right-1)
        return True
        



if __name__ == "__main__":
    s = Solution()
    # str1 = "aba"
    str1 = "abca"
    str1 = "ebcbbececabbacecbbcbe"
    print(s.validPalindrome(str1))