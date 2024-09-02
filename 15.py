def number(num):
    """
    its for user number
    """
    #variables
    num_str = str(num)
    mun = num_str[::-1]
    reversed_num = int(mun)
    
    #if and else
    if num == reversed_num:
        return "yes"
    else:
        return "no"

#input n and call fanction
n = int(input("Enter a number: "))
result = number(n)
print(result)
