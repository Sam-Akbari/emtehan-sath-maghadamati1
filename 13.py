def sekar_namak_estan():
    """
    it is for ills shekar and namak estans
    """
    #inputs n , k , p , q
    n = int(input("Enter n: "))
    k = int(input("Enter k: "))
    p = int(input("Enter p: "))
    q = int(input("Enter q: "))
    
    #their -
    nk = n - k
    pq = p - q
    
    #if and elifs
    if pq == nk:
        print("Equal")
    elif nk >= pq:
        print("Shekarestan")
    elif pq>= nk:
        print("Namakestan")
#call fanctoin
sekar_namak_estan()