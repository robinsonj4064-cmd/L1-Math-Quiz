print("😝❤️HIII Welcome to my Amazeing math quiz :p ❤️")
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
