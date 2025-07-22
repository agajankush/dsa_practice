def find_zeros(n, count):
    if n == 0:
        return count
    
    if n % 10 == 0:
        return find_zeros(n//10, count + 1)
    else:
        return find_zeros(n//10, count)

print(find_zeros(3020403,0))