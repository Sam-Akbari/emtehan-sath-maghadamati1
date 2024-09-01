def game():
    """
    it is for numbr game 
    """
    try:
        #input of user
        num = int(input("Game: "))

        #swap number
        ones_digit = num % 10
        tens_digit = (num // 10) % 10

        # and in the end:
        if ones_digit > tens_digit:
            print(ones_digit - tens_digit)
        else:
            print(tens_digit - ones_digit)
    #for erore
    except ValueError:
        print("Erore!")


game()#call fanction
