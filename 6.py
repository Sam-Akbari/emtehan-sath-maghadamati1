def calculate_floor(string):
    """
    stairs fanction
    """
    # U and D
    u_d = {'D': -1, 'U': 1}

    # stairs
    total_floor = 0
    for i in string:
        if i in u_d:
            total_floor += u_d[i]
    final_floor = total_floor

    print(final_floor)

# input and finish
user_input = input("Go: ")
result = calculate_floor(user_input)
