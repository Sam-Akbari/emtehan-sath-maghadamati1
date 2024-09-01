def get_title(travels):
    """
    if is for name of men
    """
    #if this is yyy
    if travels == 'YYY':
        print("Haji")
    #if this is yny
    elif travels == "YNY":
        print("Haji")
    #if this is nnn
    elif travels == 'NNN':
        print("Agha")
    #if this is nny
    elif travels == 'NNY':
        print("Mashti")
    #if this is nyy
    elif travels == 'NYY':
        print("Karbalaee")
    #otherwise
    else:
        return "Agha"#it is agha

#call fanction and input
travels_input = input("Subject: ")
result = get_title(travels_input)

