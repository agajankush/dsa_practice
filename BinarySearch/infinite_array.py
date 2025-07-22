
def find_index(arr, target):
    start = 0
    end = 1
    while arr[end] < target:
        temp = end + 1
        end = end + (end - start) * 2
        start = temp
    
    return binary_search(arr, target, start, end)

def binary_search(arr, target, start, end):
    while start <= end:
        mid = start + (end - start) // 2
        if target < arr[mid]:
            end = mid - 1
        elif target > arr[mid]:
            start = mid + 1
        else:
            return mid
    return -1
            
if __name__ == "__main__":
    array = [1, 2, 5, 7, 8, 9, 10]
    target = 5
    print(find_index(array, target))