def quickSearch(seq):
    if seq == []:
        return []
    else:
        pivot = seq[0]
        lesser = quickSearch([x for x in seq[1:] if x < pivot])
        greater = quickSearch([x for x in seq[1:] if x >= pivot])
        return lesser + [pivot] + greater

if __name__ == '__main__':
    seq = [4, 5, 67, 34, 1, 0, -45, -1, 87, -12]
    print(quickSearch(seq))
