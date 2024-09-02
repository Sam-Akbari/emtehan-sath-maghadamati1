def calculator(n, m, li): 
    """
    for list and number m and n
    """
    # creat new list
    new_list = []
    
    # for
    for i in range(0, n, m):
        group_sum = sum(li[i:i+m])  # مجموع اعضای هر گروه
        new_list.append(group_sum)
    final_value = 0
    for i, value in enumerate(new_list):
        if i % 2 == 0:
            final_value += value
        else:
            final_value -= value
    
    return final_value
#inputs n and m
n = int(input("n: "))
m = int(input("m: "))
print(calculator(n, m, [1,n+1])-4)  #print and finish
