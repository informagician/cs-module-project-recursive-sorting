# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    print(arrA,arrB)
    # Your code here

    for k in range(0, elements):
        if len(arrA) > 0 and len(arrB) > 0 and arrA[0] <= arrB[0]:
            merged_arr[k] = arrA.pop(0)
        elif len(arrA) > 0 and len(arrB) > 0 and arrA[0] > arrB[0]:
            merged_arr[k] = arrB.pop(0)
        elif len(arrA) > 0:
            merged_arr[k] = arrA.pop(0)
        elif len(arrB) > 0:
            merged_arr[k] = arrB.pop(0)
            
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
        merge(left,right)
    return arr
    

# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here


    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here


    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
