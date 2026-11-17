"""
3 functions to update user status throughout the game.
total_questions_func() function determines the number of questions in the specific quiz that the user takes
    based on the time they wake up (For example, if they wake up later, they will get fewer questions, 
    so their state during the game will be calculated differently).
percentage_finished() function determines the percent of the game that the user has finished.
update_progress_bar() funciton creates a progress bar based on the percent complete using the '=' character.
"""

def total_questions_func(wake_up_time):
    """
    Determines the total nubmer of questions in the quiz based on what time the user wakes up in the game.
    Inputs:
        wake_up_time: a float; the time the user wakes up in hours past midnight.
    Outputs:
        number_of_questions: an int; the number of questions in the version of the quiz the user receives.
    """
    if wake_up_time >= 9.5:
        number_of_questions = 1
    elif wake_up_time >= 9:
        number_of_questions = 6
    elif wake_up_time >= 8:
        number_of_questions = 7
    elif wake_up_time >= 7:
        number_of_questions = 10
    return number_of_questions

def percentage_finished(total_questions, question_number):
    """
    Updates the percentage the user is complete with the game/quiz.
    Inputs:
        total_questions: an int; the total number of questions in the version of the quiz the user receives.
        question_number: an int; the question number the user is on.
    Outputs:
        percentage_finished: an int; the (rounded) percentage that the user has completed the game/quiz.
    """
    percentage_finished = int((question_number / total_questions) * 100)
    return percentage_finished

def update_progress_bar(total_questions, question_number):
    """
    Prints a progess bar based on the percentage of the game/quiz the user has completed.
    The progress bar is out of 50 (not 100) so the function converts the percentage to be out of 50.
    Inputs:
        questions_number: an int; the number of questions the user has answered
    Outputs:
        A progress bar informing the user how far they are in the game/quiz using the '=' character 
        inside square brackets
    """
    complete_section = int(percentage_finished(total_questions, question_number) / 2)
    bars = complete_section * "="
    number_spaces = (50 - complete_section) * " "
    return f"[{bars}" + f"{number_spaces}] \n"