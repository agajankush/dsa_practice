def find_index(arr, target, is_start):
    start = 0
    end = len(arr) - 1
    ans = 0
    while start <= end:
        mid = start + (end - start) // 2
        if target < arr[mid]:
            end = mid - 1
        elif target > arr[mid]:
            start = mid + 1
        else:
            ans = mid
            if is_start:
                end = mid - 1
            else:
                start = mid + 1
        
    return ans
    
if __name__ == "__main__":
    array = [1,2,4,4,4,6,7,9]
    target = 4
    start_index = find_index(array, target, 1)
    end_index = find_index(array, target, 0)
    print([start_index, end_index])