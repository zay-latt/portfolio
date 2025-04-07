def selection_sort(list_a):
    index_length = range(len(list_a)-1)
    for i in index_length:
        min_value = i  
        for j in range(i+1, len(list_a)):
            if list_a[j] < list_a[min_value]:
                min_value = j    
        if min_value != i:
            list_a[min_value], list_a[i] = list_a[i], list_a[min_value]
    return list_a

print(selection_sort([2,4,1,3,5,6,9,8,7]))