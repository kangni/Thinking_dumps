def insertion_sort(l):
    for i in range(len(l)):
        currentvalue = l[i]
        position = i
        while position > 0 and l[position - 1] > currentvalue:
            l[position] = l[position - 1]
            position -= 1
        l[position] = currentvalue
    return l


if __name__ == '__main__':
    l = [1, 5, 7, 3, 2, 9, 0, -1, -5]
    result = insertion_sort(l)
    print(result)
