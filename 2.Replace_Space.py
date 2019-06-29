# -*-coding:utf-8-*-
# 题目描述 (P51)
# 请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

# 思路
# 针对一个定长数组，如果从头到尾挨个替换的话，会涉及很多字符的移动，所以想法是从后往前，遍历到空格就替换，但是对于python其实不用这么讲究


class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        res = ''
        for ele in s:
            if ele.strip():  # strip函数是删除开头或结尾的空格或换行符，这里如果遇见一个空格，经过strip函数后，就是空了
                res += ele
            else:
                res += '%20'
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.replaceSpace('We are happy.'))
