def noroz():
    """
    this is for tools noroz(sevensin)
    """
    #tools
    sib = "sib"
    samanoo = "samanoo"
    senged = "senjed"
    serkeh = "serkeh"
    sekkeh = "sekkeh"
    sir = "sir"
    somagh = "somagh"
    #input m
    m = int(input("Enter M: "))
    #creat for
    for i in range(1,m+1):
        #print tools
        if i == 1:
            print(sib)
        elif i == 2:
            print(samanoo)
        elif i == 3:
            print(senged)
        elif i == 4:
            print(serkeh)
        elif i == 5:
            print(sekkeh)
        elif i == 6:
            print(sir)
        elif i == 7:
            print(somagh)
        else:
            print("your number should is 1 to 7!")

        
noroz()#call fanctoin