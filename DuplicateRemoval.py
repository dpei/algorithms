__author__ = 'dongpei'


a = [1,3,4,4,2,1,9]
a = [5,10,12]
a = [1,22,1,4,4,6]
# in b b[i]=1 if i is in a, b[i]=0 if i is not in a


def Duplicate_Removal(a):
    m = max(a)
    b = [0] * m
    for i in range(len(a)):
        b[a[i]-1] = 1
    temp = []
    for i in range(m):
        if b[i] != 0:
            temp = temp + [i+1]
    return temp