def fruits(h, k):
    """
    this fanction is for wattermelon and melon
    """
    #watermelon
    watermelon = h * 2

    #melon
    melon = k

    #if and else
    if watermelon == melon:
        return "YES"
    else:
        return "NO"

#inputs
h = int(input("Enter H: "))
k = int(input("Enter K: "))

#call fanctoin and end
result = fruits(h, k)
print(result)
