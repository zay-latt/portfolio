def linear_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return "Index is at ", i
    return "Index is NOT FOUND in this list"

list = [1,2,3,4,5,6,7,8,9,10]

result = linear_search(list, int(input("Enter a number to search for: ")))
print(result)