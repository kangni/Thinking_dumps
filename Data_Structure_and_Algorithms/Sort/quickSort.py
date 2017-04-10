def quick_sort(seq):
    if seq == []:
        return []
    else:
        pivot = seq[0]
        lesser = quick_sort([x for x in seq[1:] if x < pivot])
        greater = quick_sort([x for x in seq[1:] if x >= pivot])
        # 若要去重的话，去掉等于号
        return lesser + [pivot] + greater


if __name__ == '__main__':
    seq = [4, 5, 67, 34, 1, 0, -45, -1, 87, -12]
    print(quick_sort(seq))
