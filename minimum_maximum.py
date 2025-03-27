# Find the minimum value using iteration:
def min(l):
    if l == []:
        return l
    
    min = l[0]
    for i in range(len(l)):
        if l[i] < min:
            min = l[i]
    return min

print(min([]))
print(min([1,2,3,4,5]))
print(min(["a","b","c"]))



# Find the maximum value using iteration:
def max(l):
    if l == []:
        return l
    
    max = l[0]
    for i in range(len(l)):
        if l[i] > max:
            max = l[i]
    return max

print(max([]))
print(max([1,2,3,4,5]))
print(max(["a","b","c"]))