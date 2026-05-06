def int_check(question):
    """Checks users enter on integer more than / equal to 13"""

    while True:
        error = "Please enter an integer that is 1 or more."

        response = input(question)

        # check for infinite mode
        if response == "":
            return ""

        try:
            response =int(response)

            #check that the number is more than / equal to 13
            if response < 1:
                print(error)

            else:
                return response

        except ValueError:
            print(error)


            # Ask user for number of rounds / infinite mode
            num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode: ")
            # Intialise game variables
            mode = "regular"

            if num_rounds == "":
                mode = "infinite"
                num_rounds = 5