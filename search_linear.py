def linear_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

def verify(index):
    if index != -1:
        print("Index is at ", index)
    else:
        print("Index is not found in this list")

list = [1,2,3,4,5,6,7,8,9,10]

result = linear_search(list, print(int(input("Enter a number to search for: "))))
verify(result)