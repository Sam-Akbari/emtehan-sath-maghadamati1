def calculate_factorial(number):
    """
    it is factorial fanctoin for user number
    """
    result = 1#what is result?
    for i in range(1, number + 1):#creat for
        result *= i
    return result

#call fanction and input
user_input = int(input("N:"))
factorial_result = calculate_factorial(user_input)
print(factorial_result)
