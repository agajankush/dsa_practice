def check_sorted(arr, i):
    if i == len(arr) - 1:
        return True
    
    return (arr[i] < arr[i+1]) and check_sorted(arr, i+1)

print(check_sorted([1,2,3,4,3,5], 0))