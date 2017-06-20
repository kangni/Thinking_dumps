def short_bubble_sort(l):
    '''
    短冒泡，若一次遍历没有发生交换，证明列表有序，程序提前停止
    '''
    exchanges = True
    pass_num = len(l)
    while pass_num > 0 and exchanges:
        exchanges = False
        for i in range(pass_num-1):
            if l[i] > l[i + 1]:
                exchanges = True
                l[i], l[i + 1] = l[i + 1], l[i]
        pass_num -= 1


if __name__ == '__main__':
    l = [1, 5, 3, 6, 2, 78, 54]
    result = short_bubble_sort(l)
    print(result)
