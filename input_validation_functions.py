"""
4 functions to validate different forms of input.
multiple_choice_validation() function validates user input to multiple choice questions. Input must be either 
    'a', 'b', or 'c'
character_validation() function validates user input for which personality type they think they are at 
    the beginning of the game. Input must be either 'Bob', 'Stuart', or 'Kevin' (capitalization does not matter)
time_validation() function validates user input for the time they set their alarm to wake up in the morning.
    Input must be a non-negative numerical value following the 24 hour clock
math_question_validation() function validates user input for their answer to the tiebraker math question, 
    ensuring that the input is an integer.
"""

def multiple_choice_validation(user_input):
    """
    Validates user input to a multiple choice question where the answer must either be 'a', 'b', or 'c'.
    Inputs:
        user_input: a string; the user's answer to the multiple choice question.
    Outputs:
        A statment describing if the user input is valid or not; a string.
    Side effects:
        Takes input from the user if they originally give an invalid input.
    """
    while user_input != "a" and user_input != "b" and user_input != "c":
        user_input = input("Not a valid input! Must respond with 'a', 'b', or 'c'. Try again: ")
    return user_input

def character_validation(user_guess_input):
    """
    Validates user input of thier guess of what minion they are.
    Inputs:
        user_guess_input: a string; inputted by the user, thier guess of what minion they are.
    Outputs:
        A statement informing the user of an invalid input.
        A new string of the user's guess if their first guess was invalid.
    Side effects:
        Takes input from the user if they originally give an invalid input
    """
    while user_guess_input.capitalize() != "Bob" and user_guess_input.capitalize() != "Stuart" and user_guess_input.capitalize() != "Kevin":
        user_guess_input = input("Invalid input! Must type either 'Bob', 'Stuart', or 'Kevin'. Try again: ")
    return user_guess_input

def time_validation():
    """
    Asks user to input the time they want to set thier alarm for and validates the input to ensure it is 
        a non-negative numerical value.
    Inputs:
        N/A
    Outputs:
        alarm_time_input: a float; the validated alarm set by the user in hours after midnight.
    Side effects:
        Prints statements outside of the return value and takes inputs from the user.
    """
    while True:
        try:
            alarm_time_input = float(input("What time do you want to set your alarm for? Input in hours after midnight "
                                           "(For example, if 8:30am, type 8.5). If setting your alarm for the afternoon, "
                                           "use 24-hour clock (for example, 1pm is 13) "))
            if alarm_time_input < 0:
                alarm_time_input = print("Time cannot be negative! Try again: ")
                continue
            elif alarm_time_input > 24:
                alarm_time_input = print("You must set the alarm within one day. Input must be no more than 24 hours "
                                         "after midnight.")
                continue
        except ValueError as e:
            alarm_time_input = print("Invalid input! Must input a numerical value in hours after midnight "
                                     "(for example, 8:30 would be 8.5). Try Again: ")
        else:
            break
    return alarm_time_input

def math_question_validation():
    """
    Validates that the answer a user provides to a math question is an integer and lets the user try again if it is not.
    Inputs:
        N/A
    Outputs:
        math_answer: an int; the user's answer to the math problem.
    Side effects:
        Prints statements outside of the return value and takes user input.
    """
    while True:
        try:
            math_answer = int(input("What is (7+13)/2 equal to? Please type in an integer value. "))
        except ValueError as e:
            math_answer = print("Input must be an integer! Try again: ")
        else:
            break
    return math_answer