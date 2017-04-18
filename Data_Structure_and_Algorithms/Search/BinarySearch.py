def BinarySearch(a_list, item):
    first = 0
    last = len(a_list) - 1
    found = False

    while first <= last and not found:
        middle = (first + last) >> 1
        if item < a_list[middle]:
            last = middle
        elif item > a_list[middle]:
            first = middle + 1
        else:
            return middle
            found = True

    return None
