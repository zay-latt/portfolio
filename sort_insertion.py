def insertion_sort(list_a):
    index_length = range(len(list_a))
    for i in index_length:
        while list_a[i-1] > list_a[i] and i > 0:
            list_a[i], list_a[i-1] = list_a[i-1], list_a[i]
            i = i-1
    return list_a
print(insertion_sort([2,4,1,3,5,6,9,8,7]))