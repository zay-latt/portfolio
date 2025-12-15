def bubble_sort(list_a):
    sorted = False

    while sorted == False:
        sorted = True
        for i in range(len(list_a)-1):
            if list_a[i-1] > list_a[i]:
                sorted = False
                list_a[i-1], list_a[i] = list_a[i], list_a[i-1]
    list_a = list_a[-1:] + list_a[:-1]

    return list_a

print(bubble_sort([0,2,4,1,3,5,6,9,8,7]))