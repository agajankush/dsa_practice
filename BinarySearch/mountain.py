
def find_peak(arr):
    start = 0
    end = len(arr) - 1
    
    while start < end:
        mid = start + (end-start) // 2
        if arr[mid] > arr[mid+1]:
            end = mid
        else:
            start = mid + 1
    return start

if __name__ == "__main__":
    arr = [1,2,3,5,6,7,4,3,2,1]
    print(find_peak(arr))