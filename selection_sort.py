def selectionSort(arr):
    for i in range(len(arr)):
        min= float('-inf')
        for j in range (i+1,len(arr)):
            if arr[i]> arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    return arr

print(selectionSort([456,25,45,7,8,6,89,3,6,5]))

def selct_sort(arr):
    for i in range (len(arr)-1):
        min=i
        for j in range(i+1, len(arr)):
            if arr[j]<arr[min]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]
    return arr
print(selct_sort([45,25,4,1,6,87,62]))