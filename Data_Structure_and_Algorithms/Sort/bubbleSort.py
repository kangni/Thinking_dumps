def bubbleSort(l):
    exchanges = True
    pass_num = len(l) - 1
    while pass_num > 0 and exchanges:
        exchanges = False
        for i in range(pass_num):
            if l[i] > l[i + 1]:
                exchanges = True
                l[i], l[i + 1] = l[i + 1], l[i]
        pass_num -= 1


if __name__ == '__main__':
    l = [1, 5, 3, 6, 2, 78, 54]
    result = bubbleSort(l)
    print(result)
