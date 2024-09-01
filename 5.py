def wow():
    """
    it is for O if wow
    """
    #creat try
    try:
        # creat input
        num = int(input("How many O in wow? "))

        # number of O  for wow
        print("w" + "o" * num + "w!")
    #except
    except ValueError:
        print("Erore!")

wow()
