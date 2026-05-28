import random

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

def int_check(question, easy=None, medium=None, hard=None, diabolical=None, exit_code=None):
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

quiz_list = ["easy", "medium", "hard", "xxx"]

user_choice = string_checker("Choose Level: ", quiz_list)
print("You Choose:", user_choice)

exit_code = "xxx"

# Ask user for number of questions / infinite mode
num_questions = int_check("How many questions would you like? Push <enter> for infinite mode: ")

# Initialise game variables
mode = "regular"
questions_asked = 0
questions_wrong = 0
questions_correct = 0
questions = 0
game_history = []


if num_questions == "":
    mode = "infinite"
    num_questions = 5

# Game loop starts here
while questions_asked < num_questions:
    questions_asked += 1


    # Rounds heading
    if mode == "infinite":
        questions_heading = f"\n\u221e\u221e\u221e Question {questions_asked} (Infinite Mode) \u221e\u221e\u221e"
    else:
        questions_heading = f"\n💿💿💿 Question {questions_asked} of {num_questions} 💿💿💿"

    print(questions_heading)
    print()

    if user_choice == "easy":
        # The easy questions 1-10
        questions_int1 = random.randint(1, 10)
        questions_int2 = random.randint(1, 10)
        total = questions_int1 + questions_int2
        math_expression = (f" {questions_int1} + {questions_int2}  ")
        math_answer = eval(math_expression)
        print(math_expression)
        answer = input("What is the answer? ")


    # Medium questions
    elif user_choice == "medium":
        questions_int1 = random.randint(1, 30)
        questions_int2 = random.randint(1, 30)
        total = questions_int1 + questions_int2
        math_expression = (f" {questions_int1} + {questions_int2}  ")
        math_answer = eval(math_expression)
        print(math_expression)
        answer = input("What is the answer? ")


    # Hard Questions
    else:
        questions_int1 = random.randint(1, 12)
        questions_int2 = random.randint(1, 12)
        total = questions_int1 + questions_int2
        math_expression =(f" {questions_int1} * {questions_int2}  ")
        math_answer = eval(math_expression)
        print(math_expression)
        answer = input("What is the answer? ")

    # Infinite mode questions increasing
    if mode == "infinite":
        num_questions += 1

    # Exit code
    if answer == exit_code:
        questions_asked -= 1
        break


    # Check if the user's answer matches the math answer
    try:
        if int(answer) == math_answer:
            feedback = f"Correct! Great job! {math_answer} was the right answer. "
            print(feedback)
            questions_correct += 1
        else:
            feedback = f"Incorrect. The correct answer was {math_answer}. Better luck next time!"
            print(feedback)
            questions_wrong += 1
    except ValueError:
        feedback = f"That wasn't a valid number! Counted as incorrect. The right answer was {math_answer}."
        print(feedback)
        questions_wrong += 1

    history_item = f"Round {questions_asked}: {math_expression.strip()} = {answer} | {feedback}"
    game_history.append(history_item)

if questions_asked > 0:
    # Calculate Statistics
    questions_correct_pct = (questions_correct / questions_asked) * 100
    questions_wrong_pct = (questions_wrong / questions_asked) * 100

    # Output Game Statistics
    print("\n📊📊📊 Game Statistics 📊📊📊")
    print(f"❤️ Correct: {questions_correct} ({questions_correct_pct:.1f}%) \t"
          f"😭 Wrong: {questions_wrong} ({questions_wrong_pct:.1f}%) \t")

    # Game history / Statistics area
    see_history = string_checker("\nDo you want to see your game history? ")
    if see_history == "yes":
        print("\n--- Game History ---")
        for item in game_history:
            print(item)
else:
    print("\nNo questions were completed.")

print()
print("Thanks for playing.")
