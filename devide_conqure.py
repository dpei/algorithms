__author__ = 'dongpei'

c = [1, 2.4, 2, 3.2, 4, 3.3, 3, 6, 5]

def merge_two(a,b):
    n1 = len(a)
    n2 = len(b)
    a[n1] = float("inf")
    b[n2] = float("inf")
    i = 0
    j = 0
    # Here list or tuple assignment?
    c = []
    for n in range(n1+n2):
        if a[i] < b[j]:
            c[n] = a[i]
            i += 1
        else:
            c[n] = b[j]
            j += 1
    return(c)
merge_two([1,2],[1.5, 6])



def MergeSort(c):
   n = len(c)
   if (n == 1):
       return (c)
   left = c[0:n/2]
   right = c[n/2: n]
   sorted_left = MergeSort(left)
   sorted_right = MergeSort(right)
   sorted = merge_two(sorted_left, sorted_right)
   return(sorted)

n=1
MergeSort(c)