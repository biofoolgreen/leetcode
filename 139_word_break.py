"""
给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。
示例 3：

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-break
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        lens = len(s)
        # dp[n]:表示 s 的前 n 位是否可以用 wordDict 中的单词表示
        dp = [False]*(lens+1)
        dp[0] = True
        for i in range(lens):
            for j in range(i+1, lens+1):
                # 如果前i位可以用wordDict表示，且i->j位也可以，那么前j位也可以
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
        return dp[-1]


if __name__ == "__main__":
    slu = Solution()
    s = "abcd"
    word_dict = ["a","abc","b","cd"]
    print(slu.wordBreak(s, word_dict))