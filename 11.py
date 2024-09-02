def battery(k):
    """
    it is for time battery
    """
    #if for battery
    if k <= 100 and k >= 1:
        #creat time
        time = sum(range(1,k+1))
        return time
#input and call or print fanctoin
k = int(input("K: "))
print(battery(k))