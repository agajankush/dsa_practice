def reverse_number(n, sum):
    if n == 0:
        return sum
    
    rem = n % 10
    sum = sum * 10 + rem
    return reverse_number(n//10, sum)

print(reverse_number(1234, 0))