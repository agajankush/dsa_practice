def split_array(array):
    if len(array) == 1:
        return array
    
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]
    
    left = split_array(left)
    right  = split_array(right)
    
    return merge_array(left, right)

def merge_array(left, right):
    mix = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            mix.append(left[i])
            i += 1
        else:
            mix.append(right[j])
            j += 1
        
    while i < len(left):
        mix.append(left[i])
        i += 1
    
    while j < len(right):
        mix.append(right[j])
        j += 1
    return mix

print(split_array([5,4,3,2,1])) 