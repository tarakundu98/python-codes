
def sort(arr):
    n = len(arr)
    sorted_flag = False
    
    while not sorted_flag:
        sorted_flag = True
        
        for i in range(0, n - 2, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted_flag = False
        
        for i in range(1, n - 1, 2):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted_flag = False
    
    return arr

arr = list(map(int, input("Enter array elements: ").split()))
sorted_arr = sort(arr)
print("Sorted array:", sorted_arr)