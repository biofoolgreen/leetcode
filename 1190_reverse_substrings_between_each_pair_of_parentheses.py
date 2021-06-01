"""
给出一个字符串 s（仅含有小写英文字母和括号）。

请你按照从括号内到外的顺序，逐层反转每对匹配括号中的字符串，并返回最终的结果。

注意，您的结果中 不应 包含任何括号。

 

示例 1：

输入：s = "(abcd)"
输出："dcba"
示例 2：

输入：s = "(u(love)i)"
输出："iloveu"
示例 3：

输入：s = "(ed(et(oc))el)"
输出："leetcode"
示例 4：

输入：s = "a(bcdefghijkl(mno)p)q"
输出："apmnolkjihgfedcbq"
 

提示：

0 <= s.length <= 2000
s 中只有小写英文字母和括号
我们确保所有括号都是成对出现的

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-substrings-between-each-pair-of-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        n = len(s)
        i = 0
        while i < n:
            cur_char = s[i]
            if cur_char != ")":
                stack.append(cur_char)
            else:
                # 碰到右括号就把前一个左括号间的所有元素依次出栈再入栈回stack
                c = stack.pop(-1)
                tmp = []
                while c != "(":
                    tmp.append(c)
                    c = stack.pop(-1)
                for c in tmp:
                    stack.append(c)
            i += 1
        return "".join(stack)


if __name__ == "__main__":
    sl = Solution()
    # s = "(ed(et(oc))el)"
    s = "a(bcdefghijkl(mno)p)q"
    print(sl.reverseParentheses(s))