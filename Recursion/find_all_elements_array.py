def find_all_elements_array(array, i, target, list):
    if i == len(array):
        return list
    
    if array[i] == target:
        list.append(i)
    
    return find_all_elements_array(array, i+1, target, list)

print(find_all_elements_array([1,2,3,4,5,5,5,8,9,5], 0, 5, []))