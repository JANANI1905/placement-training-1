def append_middle(s1, s2):
    print("Original Strings are", s1, s2)
    mi = int(len(s1) / 2)
    x = s1[:mi]
    x = x + s2
    x = x + s1[mi:]
    print("After appending new string in middle:", x)
s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")
append_middle(s1, s2)
