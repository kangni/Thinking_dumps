# -*- coding: utf-8 -*-

# 最小的k个数

# 输入n个整数，找出其中最小的k个数。
# 例如输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。
import heapq

k = 4
numbers = [4, 5, 1, 6, 2, 7, 3, 8]
print(heapq.nsmallest(k, numbers))
