def binary_search(l, target):
    first = 0
    last = len(l) - 1

    while first <= last:
        midpoint = (first + last)//2
        if l[midpoint] == target:
            return midpoint
        elif l[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return -1

def verify(index):
    if index != -1:
        print("Index is at ", index)
    else:
        print("Index is not found in this list")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = binary_search(numbers, print(int(input("Enter a number to search for: "))))
verify(result)