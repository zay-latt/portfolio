def is_anagram(s1, s2):
    s1 = s1.lower().replace(" ", "")
    s2 = s2.lower().replace(" ", "")

    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)

s1 = input("Enter first word: ")
s2 = input("Enter second word: ")

print(is_anagram(s1, s2))