# -*-coding:utf-8-*-
# 题目描述 (P44)
# 在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，
# 每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

# 思路
# 数组是一个左右、上下分别有序的，可从右上遍历，如果比右上的大，这一列有可能，否则往左；


class Solution:
    # array 二维列表
    def Find(self, target, array):
        # 容错
        if not array:
            return False
        rows = len(array)-1
        cols = len(array[0])-1
        i = 0
        j = cols
        while i <= rows and j >= 0:
            if target < array[i][j]:  # 这一列下面的数比它都大，不用看了
                j -= 1
            elif target > array[i][j]:  # 比这列第一个大，继续往下看
                i += 1
            else:  # 相等
                return True
        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.Find(7, [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]))
