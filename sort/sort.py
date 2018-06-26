import random
import math
import time

def bubblesort(arr):
    ''' bubble sort '''
    for i in range(0,len(arr)):
        for j in range(i+1, len(arr)):
            if a[j]<a[i]:
                temp = a[i]
                a[i] = a[j]
                a[j] = temp 
    return arr

def mergesort(arr):
    ''' merge sort '''
    #print ('merge sort', end = '')
    #print (arr)
    if len(arr) <= 1:
        return arr
    else:
        return merge(mergesort(arr[:int(len(arr)/2)]), mergesort(arr[int(len(arr)/2):]))

def merge(arr1, arr2):
    #print ('merging ', end = '')
    #print (arr1, end = '')
    #print (arr2)
    arr = []
    cur1 = 0
    cur2 = 0
    for i in range(0, len(arr1)+len(arr2)):
        if arr1[cur1] <= arr2[cur2]:
            arr.append(arr1[cur1])
            cur1 = cur1 + 1
        else:
            arr.append(arr2[cur2])
            cur2 = cur2 + 1
        
        if cur1 == len(arr1):
            arr = arr + arr2[cur2:]
            break
        if cur2 == len(arr2):
            arr = arr + arr1[cur1:]
            break
    #print ('return merged', end = '')
    #print (arr)
    return arr

if __name__ == '__main__':
    a = []
    for i in range(0,10000):
        a.append(random.randint(1,2000))
    
    t1 = time.time()
    print (bubblesort(a))
    t2 = time.time()
    print (mergesort(a))
    t3 = time.time()
    print(t2 - t1)
    print(t3 - t2)