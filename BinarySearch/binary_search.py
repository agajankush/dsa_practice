def binarySearch(arr, target):
    left = 0
    right = len(arr)
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    return -1

def ceiling_floor(arr, target, is_ceiling):
    left = 0
    right = len(arr)
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
    if is_ceiling == True:
        return arr[left]
    return arr[right]

if __name__ == "__main__":
    array = [1,2,3,6,7,8,9]
    target = 10
    print(ceiling_floor(array, target, False))
        