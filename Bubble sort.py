__author__ = 'dongpei'
# not complete



def bubble_sort (alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i+1]
                alist[i+1] = alist[i]
                alist[i] = temp

    return(alist)

alist = [54,26,93,17,77,31,44,55,20]
bubble_sort(alist)