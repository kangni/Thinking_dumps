def shell_sort(data):
    sublist_count = len(data) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(data, start_position, sublist_count)
        sublist_count = sublist_count // 2
    return data

def gap_insertion_sort(data, start, gap):
    for i in range(start + gap, len(data), gap):
        current_val = data[i]
        position = i
        while position > 0 and data[position - gap] > current_val:
            data[position] = data[position - gap]
            position = position - gap
        data[position] = current_val

alist = [85, 35, -23, 0, 12, 43, -12, 0, 32, 98, -65]
print(shell_sort(alist))