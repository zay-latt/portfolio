def insertion_sort(list_a):
    for i in range(len(list_a)):
        while list_a[i-1] > list_a[i] and i > 0:
            list_a[i-1], list_a[i] = list_a[i], list_a[i-1]
            i -= 1            
    return list_a
print(insertion_sort([2,4,1,3,5,6,9,8,7,0]))