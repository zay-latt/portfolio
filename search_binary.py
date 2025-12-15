def binary_search(l, target):
    first = 0
    last = len(l)

    while first <= last:
        midpoint = (first + last)//2
        if l[midpoint] == target:
            return "Index is at ", midpoint
        elif l[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return "Index is NOT FOUND in this list"

list = [1,2,3,4,5,6,7,8,9,10]

result = binary_search(list, int(input("Enter a number to search for: ")))
print(result)