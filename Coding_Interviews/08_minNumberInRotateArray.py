# -*- coding: utf-8 -*-

# 旋转数组中的最小数字

# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
# 输入一个递增排序的数组的一个旋转，输出旋转数组中的最小元素。

# 例如数组{3, 4, 5, 1, 2}为{1, 2, 3, 4, 5}的一个旋转，最小值为 1


def min_number_in_rotate_array(rotate_array):
    """
    Python大法好
    """
    return min(rotate_array)

if __name__ == '__main__':
    a_array = (3, 4, 5, 1, 2)
    result = min_number_in_rotate_array(a_array)
    print(result)
