def bubble_sort(list_a):
    index_length = len(list_a)-1
    sorted = False

    while sorted == False:
        sorted = True
        for i in range(index_length):
            if list_a[i] > list_a[i+1]:
                sorted = False
                list_a[i], list_a[i+1] = list_a[i+1], list_a[i]

    return list_a

print(bubble_sort([2,4,1,3,5,6,9,8,7]))