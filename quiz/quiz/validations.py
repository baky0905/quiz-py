def validate_user_input(input):
    try:
        int(input)
        return int(input)
    except ValueError:
        print("Your input is a string! Please try again!")
        return False
