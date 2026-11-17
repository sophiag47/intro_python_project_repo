"""
6 functions that each determine different parts of playing the game.
choose_breakfast() function determines which minion the user is most like based on their breakfast choice, 
    which is inputted by the user.
morning_activity() funciton determines which minion the user is most like based on their decision for what to do 
    for a morning activity. It also asks the user follow up quesitons if they choose to go to the gym, 
    and determines which minion they are most like based on their chocies at the gym.
where_sit() function determines which minion the user is most like based on thier decision for where to sit in class.
pick_lunch() function determines which minion the user is most like based on what they decide to eat for lunch.
pick_work() function determines which minion the user is most like based on their decisions at work.
pick_library() function determines which minion the user is most like based on which library they decide to go to.
"""

import random

import input_validation_functions

import user_status_functions

def choose_breakfast(breakfast_location):
    """
    Determines which minion the user is most like based on their decisions for what to do for breakfast.
    Inputs:
        breakfast_location: a string; inputted by user, the place they choose to get breakfast
    Outputs:
        A string; the minion the user is most like based on their breakfast choices
    Side effects:
        Prints a statement to inform the user what is happening in the day in the life after each decision
    """
    validated_breakfast_location = input_validation_functions.multiple_choice_validation(breakfast_location)
    if validated_breakfast_location == "a":     # location 'a' is Kimball
        print("\nYou go to Kimball for breakfast and take a slower morning. Then you head to class")
        return "Bob"
    elif validated_breakfast_location == "b":    # location 'b' is Cool Beans
        people_in_line = random.randint(0, 30)
        if people_in_line >= 20:
            print(f"\nThere are {people_in_line} people already in the Cool Beans line! "
                  "It takes a long time to get your order and you rush to class")
        elif people_in_line >= 10:
            print(f"\nThere are {people_in_line} people in the Cool Beans line. You don't get your food immediately, "
                  "but it doesn't take too long. You eat and go to class")
        else:
            print(f"\nThere are only {people_in_line} people in the Cool Beans line! You get your food quickly "
                  "and have time to look at your email before class.")
        return "Stuart"
    elif validated_breakfast_location == "c":    # location 'c' is the user cooks themselves
        print("\nYou cook yourself a nice breakfast, wash the dishes, and head to class")
        return "Kevin"


def morning_activity(what_morning_activity_is):
    """
    Return the minion the user is most like based on the user's decision of what to do for their morning activity.
    Inputs:
        what_morning_activity_is: a string; inputted by the user, a morning activity
    Outputs
        A string; the minion the user is most like based on their morning activity choices
    Side effects:
        Prints a statement to inform the user what is happening in the day in the life after each decision.
        Asks input from the user in certain scenarios
    """
    validated_morning_activity = input_validation_functions.multiple_choice_validation(what_morning_activity_is)
    print("\nProgress: " + user_status_functions.update_progress_bar(10, 3))
    if validated_morning_activity == "a":     # morning activity 'a' is go to the gym
        treadmills_open = random.choice([True, False])
        if treadmills_open:
            print("There are treadmills open so you do a running workout. Then you go back to the room and shower.")
            treadmill_activity = input("What do you do on the treadmill? Type 'a' for sprints, 'b' for distance run, "
                                       "or 'c' just run with no goal? ")
            treadmill_activity = input_validation_functions.multiple_choice_validation(treadmill_activity)
            print("Progress: " + user_status_functions.update_progress_bar(10, 4))
            if treadmill_activity == "a":   # treadmill activity 'a' is sprints
                return "Stuart"
            elif treadmill_activity == "b":   # treadmill activity 'b' is distance run
                return "Kevin"
            elif treadmill_activity == "c":     # treadmill activity 'c' is no plan
                return "Bob"
        else:
            print("You planned to go on the treadmill but there are no treadmills open. :( What do you want to do now?")
            new_gym_activity = input("Type 'a' for lift, 'b' for wait for a treadmill, or 'c' for go back to your room. ")
            new_gym_activity = input_validation_functions.multiple_choice_validation(new_gym_activity)
            print("\nProgress: " + user_status_functions.update_progress_bar(10, 4))
            if new_gym_activity == "a":   # decision 'a' is lift
                return "Kevin"
            elif new_gym_activity == "b":  # decision 'b' is wait for a treadmill
                return "Bob"
            elif new_gym_activity == "c":    # decision 'c' is go back to room
                return "Stuart"
    elif validated_morning_activity == "b":   # morning activity 'b' is go to the library
        print("\nYou go to the library and get some work done before class.")
        return "Kevin"
    elif validated_morning_activity == "c":    # morning activity 'c' is hang out with friends
        print("\nYou hang out with some friends before class.")
        return "Bob"


def where_sit(input_where_sit):
    """
    Returns the minion the user is most like based on where they sit in class.
    Inputs:
        input_where_sit: a string; inputted by the user, a letter 'a', 'b', or 'c' corresponding with where they
            sit in class.
    Outputs:
        A string: the minion that the user is most like based on where they choose to sit in class.
    """
    validate_sit = input_validation_functions.multiple_choice_validation(input_where_sit)
    if validate_sit == "a":
        return "Kevin"
    elif validate_sit == "b":
        return "Stuart"
    elif validate_sit == "c":
        return "Bob"

def pick_lunch(input_lunch):
    """
    Returns the minion the user is most like based on what they choose to eat for lunch.
        Inputs:
            input_where_sit: a string; inputted by the user, a letter 'a', 'b', or 'c' corresponding to what they eat
                for lunch.
        Outputs:
            A string: the minion that the user is most like based on what they choose to eat for lunch.
    """
    validate_lunch = input_validation_functions.multiple_choice_validation(input_lunch)
    if validate_lunch == "a":
        return "Stuart"
    elif validate_lunch == "b":
        return "Bob"
    elif validate_lunch == "c":
        return "Kevin"

def pick_work(input_work):
    """
    Returns the minion the user is most like based on what they do at work.
        Inputs:
            input_where_sit: a string; inputted by the user, a letter 'a', 'b', or 'c' corresponding to what they do
                at work.
        Outputs:
            A string: the minion that the user is most like based on what they do at work.
    """
    validate_work = input_validation_functions.multiple_choice_validation(input_work)
    if validate_work == "a":
        return "Bob"
    elif validate_work == "b":
        return "Stuart"
    elif validate_work == "c":
        return "Kevin"

def pick_library(input_library):
    """
    Returns the minion the user is most like based on which library they choose to go to.
        Inputs:
            input_where_sit: a string; inputted by the user, a letter 'a', 'b', or 'c' corresponding to which library
                they choose to go to.
        Outputs:
            A string: the minion that the user is most like based on which library they choose to go to.
    """
    validate_library = input_validation_functions.multiple_choice_validation(input_library)
    if validate_library == "a":
        return "Kevin"
    elif validate_library == "b":
        return "Stuart"
    elif validate_library == "c":
        return "Bob"