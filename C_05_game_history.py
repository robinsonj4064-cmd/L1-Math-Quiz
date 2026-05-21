import random


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

quiz_list = ["easy", "medium", "hard", "diabolical", "xxx"]

user_choice = string_checker("Choose Level: ", quiz_list)
print("You Choose:", user_choice)



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

    if user_choice == quiz_list:
        questions_int1 = random.randint(1, 10)
        questions_int2 = random.randint(1, 10)

        total = questions_int1 + questions_int2
        print(f" {questions_int1}\t + {questions_int2}\t = {total}\t")
        print()

result = int_check(questions_asked, quiz_list)

if result == "Wrong":
    questions_wrong += 1
    feedback = "😭😭 Wrong! 😭😭"
else:
    feedback = "❤️❤️ Correct!!!! ❤️❤️"

if questions_asked > 0:
    # Calculate Statistics
    questions_asked = questions - questions_correct - questions_wrong
    questions_correct = questions_correct / questions_asked * 100
    questions_wrong = questions_wrong / questions_asked * 100
    percent_tied = 100 - questions_correct - questions_wrong


round_feedback = f"{user_choice} vs {questions}, {feedback}"
history_item = f"Round: {questions_asked} - {round_feedback}"

print(round_feedback)
game_history.append(history_item)

# Output Game Statistics
print("📊📊📊 Game Statistics 📊📊📊")
print(f"❤️ Correct: {questions_correct:.2f} \t"
      f"😭 Wrong: {questions_wrong:.2f} \t")

# initialise list to hold game history

# Game history / Statistics area
see_history = string_checker("\nDo you want to see your game history? ")
if see_history == "yes":

    for item in game_history:
        print(item)

print()
print("Thanks for playing.")