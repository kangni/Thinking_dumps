def quick_sort(seq):
    if len(seq) < 2:
        return seq
    else:
        pivot = seq[0]
        lesser = [x for x in seq[1:] if x < pivot]
        greater = [x for x in seq[1:] if x >= pivot]
        # 若要去重的话，去掉等于号
        return quick_sort(lesser) + [pivot] + quick_sort(greater)


if __name__ == '__main__':
    seq = [4, 5, 67, 34, 1, 0, -45, -1, 87, -12]
    print(quick_sort(seq))
