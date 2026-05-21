print("😝❤️HIIIIIII Welcome to my Amazeing math quiz :p ❤️")
print()

#functions go here

def yes_no(question):
    """Checks user response to a question is yes / no (y/n), return 'yes' or 'no'"""

    while True:

        response = input(question).lower()

        #check the user say yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes / no")


def instructions():
    """Shows user instructions"""

    print("This is my math quiz for some basic facts i made to have fun and maybe have a challenge for some people, you can choose easy, normal or hard maybe an other secret mode :p")


#Main routine

# ask the user if they want instructions (check they said yes / no)
want_instructions = yes_no("Do you want to see the instructions? ").lower()

# Display the instructions if the user want to see them...
if want_instructions == "yes":
    instructions()

print()
print("Program continues")

def string_checker(question, valid_ans=('yes', 'no')):

 error = f"Please enter a valid option from the following list: {valid_ans}"

 while True:

    """Checks users enter either the first letter of the
    full word based on a series of valid answers"""


    # Get user response and make sure it's lowercase
    user_response = input(question).lower()

    for item in valid_ans:
        # check if the user response is a word in the list
        if item == user_response:
            return item

         # check if the user response is the same as
         # the first letter of an item in the list
        elif user_response == item[0]:
            return item

    # print error if user does not enter something that is valid
    print(error)
    print()

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

quiz_list = ["easy", "medium", "hard", "diabolical", "xxx"]

user_choice = string_checker("Choose Level: ", quiz_list)
print("You Choose:", user_choice)



# Ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? Push <enter> for infinite mode: ")
# Initialise game variables
mode = "regular"
questions_asked = 0


if num_rounds == "":
    mode = "infinite"
    num_rounds = 5


# Game loop starts here
while questions_asked < num_rounds:
    questions_asked += 1

    # Rounds heading
    if mode == "infinite":
        rounds_heading = f"\n♾️♾️♾️ Round {questions_asked} (Infinite Mode) ♾️♾️♾️"
    else:
        rounds_heading = f"\n💿💿💿 Round {questions_asked} of {num_rounds} 💿💿💿"

    print(rounds_heading)
    print()

