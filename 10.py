def number(n):
    """
    it can print yes or no for number n
    """
    # creat sums
    sums = sum(i for i in range(1, n) if n % i == 0)
    
    # if and else
    if sums == n:
        return "YES"
    else:
        return "NO"

# input n 
n = int(input("Enter n: "))

# print and finish
result = is_perfect_number(n)
print(result)
