# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # print(arrA,arrB)
    # Your code here
    i = 0
    j = 0

    for k in range(0, elements):
        if len(arrA) > i and len(arrB) > j:
            if arrA[i] <= arrB[j]:
                merged_arr[k] = arrA[i]
                i += 1
            else:
                merged_arr[k] = arrB[j]
                j += 1
        elif len(arrA) > i:
            merged_arr[k] = arrA[i]
            i += 1
        elif len(arrB) > j:
            merged_arr[k] = arrB[j]
            j += 1
            
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here
    first = 0
    last = len(arr) - 1

    if first < last:
        mid = len(arr) // 2
        left = merge_sort(arr[0:mid])
        right = merge_sort(arr[mid:])
        arr = merge(left,right)
    return arr
    

# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here
    print('THIS HERE',arr,start,mid,end)
    l = arr[start:mid]
    r = arr[mid:end+1]
    print(l,r)
    i = 0
    j = 0
    for k in range(start,end+1):
        if len(l) > i and len(r) > j:
            if l[i] <= r[j]:
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
        elif len(l) > i:
            arr[k] = l[i]
            i += 1
        elif len(r) > j:
            arr[k] = r[j]
            j += 1

    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here
    # print(arr,l,r)
    if l < r:
        mid = (l + r) // 2
        merge_sort_in_place(arr,l,mid)
        merge_sort_in_place(arr,mid+1,r)
        arr = merge_in_place(arr,l,mid,r)

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
