def max_tuple(t):
    max=t[0]
    for i in t:
        if i>max:
            max=i
    return max
T=(1,2,3,4,5)
print(max_tuple(T))