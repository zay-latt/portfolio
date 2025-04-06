def quick_sort(list_a):
    index_length = len(list_a)
    if index_length <= 1:
        return list_a
    else:
        pivot = list_a.pop()

    items_greater = []
    items_lesser = []

    for item in list_a:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lesser.append(item)

    return quick_sort(items_lesser) + [pivot] + quick_sort(items_greater)

print(quick_sort([2,4,1,3,5,6,9,8,7]))
print(quick_sort(["c", "a", "b"]))