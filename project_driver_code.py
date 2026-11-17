"""
Personality quiz "What minion are you?" based on what the user chooses to do during a typical day-in-the-life 
of a college student. User wins the game if they correctly guess which minion they will be based on 
how they go about a day in the life of a college student.
"""

import random

import input_validation_functions

import game_play_functions

import user_status_functions

def personality_type_status(all_responses, new_type):
    """
    After each question in the quiz, this function updates the dictionary that tracks the user's responses by increasing
        the count of the minion that aligns most with the user's response by 1.
    Inputs:
        all_responses: a dict; the dictionary of peronality types and their counts from all the questions 
            and user input answers.
            Keys are personality types, values are how often a user response corresponds to that personality type.
        new_type: a string; the personality type that aligns with the user's answer to a question in the quiz
    Outputs:
        an updated all_responses dictionary
    """
    all_responses[new_type] += 1
    return all_responses

def your_personality(dict_of_answers, option_one, option_two, option_three):
    """
    Takes the dictionary updated thorughout the game of the counts of each personality type that aligns with each
        user's responses to quiz question.
    Finds the personality type with the highest corresponding count, which is the personality that user is most like.
    If there is a tie between two or three personality types, the function will return False so that there 
        can be a tiebreaker question outside the function.
    Inputs:
        dict_of_answers: a dict; the dictionary of peronality types and their counts from all the questions 
            and user input answers.
            Keys are personality types, values are how often a user response corresponds to that personality type.
        option_one: a string; one option of personality types that might appear in the dictionary.
        option_two: a string; one option of personality types that might appear in the dictionary.
        option_three: a string; one option of personality types that might appear in the dictionary.
    Outputs:
        The element of that dictionary with the highest count, or False (a bool) if there is a tie.
    """
    winning_personality = max(dict_of_answers[option_one], dict_of_answers[option_two], dict_of_answers[option_three])
    if winning_personality == dict_of_answers[option_one] and winning_personality == dict_of_answers[option_two] and winning_personality == dict_of_answers[option_three]:
        return False
    elif winning_personality == dict_of_answers[option_one] and winning_personality == dict_of_answers[option_two]:
        return False
    elif winning_personality == dict_of_answers[option_one] and winning_personality == dict_of_answers[option_three]:
        return False
    elif winning_personality == dict_of_answers[option_two] and winning_personality == dict_of_answers[option_three]:
        return False
    elif winning_personality == dict_of_answers[option_one]:
        return option_one
    elif winning_personality == dict_of_answers[option_two]:
        return option_two
    elif winning_personality == dict_of_answers[option_three]:
        return option_three

def test_if_player_wins(dict_of_answers, option_one, option_two, option_three, what_user_guessed):  
    """
    Tests if the personality type the user guessed they would be matches thier result.
    Inputs:
        dict_of_answers: a dict; the dictionary of peronality types and their counts from all the questions 
            and user input answers.
            Keys are personality types, values are how often a user response corresponds to that personality type.
        option_one: a string; one option of personality types that might appear in the dictionary.
        option_two: a string; one option of personality types that might appear in the dictionary.
        option_three: a string; one option of personality types that might appear in the dictionary.
    Outputs:
        a string telling the user if they won or lost.
    """
    if your_personality(dict_of_answers, option_one, option_two, option_three) == what_user_guessed.capitalize():
        return f"You guessed {what_user_guessed}. YOU WIN! Your guess matches the minion that you are most like."
    else:
        return f"You guessed {what_user_guessed}. YOU LOSE! Your guess did not match the minion you are most like."

def when_wake_up(time_of_alarm):
    """
    Determines what time the user wakes up based on when they set their alarm and if they wake up at their 
    first alarm or not, which is random.
    Inputs:
        user_alarm: a float; the time (in hours past midnight) the user sets their alarm, inputted by the user.
    Outputs:
        a float; the time the user wakes up in hours past midnight.
    Side effects:
        Prints statements outside of the return value.
    """
    up_at_alarm = random.choice([True, False])
    while up_at_alarm == False:
        time_of_alarm += 0.2
        print(f"You are very tired. You have to hit snooze. Now it is {time_of_alarm:.2f} hours past midnight.")
        up_at_alarm = random.choice([True, False])
    if up_at_alarm == True:
        wake_up = time_of_alarm
    return wake_up

if __name__ == "__main__":
    
    print("\nGame Instructions: \n\n"
    "This game takes you through a day-in-the-life of a college student. \n" 
    "There are multiple decisions to be made each day, " 
        "and each decision tells you something about your personality. \n" 
    "Based on your decisions during this day-in-the-life, the game will be able to " 
         "tell you what minion you are most like, either Bob, Stuart, or Kevin. \n"
    "For each decision that needs to be made in the day, you will have multiple choice " 
        "option between 3 options. Type 'a', 'b', or 'c; based on your preference. \n"
    "Before you start the day, you will place your guess of which of the three minions " 
        "you think you are most like. \n"
    "You will win the game if the minion you guessed you are most like matches the minion that you are " 
        "most like based on this day-in-the-life. \n"
    "You lose if your guess doesn't match the results of the personality test, or if you are late to class. \n"
    "After every question there will be a progress bar showing you how far along you are in the game. \n"
    "Good luck! Have fun!\n")

    user_guess = input("What minion do you think you are most like? Options are Bob, Stuart, and Kevin."
    "Type in the name of the minion you think you are most like. ")
    validated_guess = input_validation_functions.character_validation(user_guess)

    personality_type_answers = {"Kevin": 0, "Bob": 0, "Stuart":0}
    
    print("\nTime to set your alarm. Your first class is at 9:30, but set it earlier if you want to have time "
           "to go to the gym or the library before class.")
    alarm = input_validation_functions.time_validation()

    time_wake_up = when_wake_up(alarm)
    if time_wake_up < 7:    # If they wake up before 7, they are prompted to go back to sleep. Before 7 is too early for a college student!
        while time_wake_up < 7:
            print(f"It is only {time_wake_up:.2f} hours after midnight! Go back to bed!")
            time_wake_up += 0.5
        print(f"It is now {time_wake_up:.2f} hours after midnight.")
    
    print(f"You wake up at {time_wake_up:.2f} hours after midnight.")

    total_questions = user_status_functions.total_questions_func(time_wake_up)

    print("\nProgress: " + user_status_functions.update_progress_bar(total_questions, 1))
   
    if time_wake_up >= 9.5:
        print("\nYou missed class! You automatically lose the game and will never know which minion you are most like. :(")
    else:
        if time_wake_up >= 9:
            personality_type_status(personality_type_answers, "Stuart")
            print("You rush to class but you make it there in time!")
        elif time_wake_up >= 8:     # If they wake up between 8 and 9, they don't have time for a morning activity but they do have time for breakfast.
            personality_type_status(personality_type_answers, 'Bob')
            what_breakfast = input("Where do you want to get breakfast? Type 'a' for Kimball Dining Hall, "
                                   "'b' for Cool Beans Cafe, and 'c' for cook yourself. ")
            breakfast_personality = game_play_functions.choose_breakfast(what_breakfast)
            print("\nProgress: " + user_status_functions.update_progress_bar(total_questions, 2))
            personality_type_status(personality_type_answers, breakfast_personality)
        elif time_wake_up >= 7:     # If they wake up between 7 and 8, they have time for a morning activity and breakfast
            personality_type_status(personality_type_answers, "Kevin")
            # morning activity
            what_activity = input("You have time for a morning activity. \nWhat do you want to do? Type "
                                  "'a' for go to the gym, 'b' for go to the library, or 'c' for hang out with friends. ")
            activity_personality = game_play_functions.morning_activity(what_activity)
            personality_type_status(personality_type_answers, activity_personality)
            # breakfast
            what_breakfast = input("Where do you want to get breakfast? Type 'a' for Kimball Dining Hall, "
                                   "'b' for Cool Beans Cafe, and 'c' for cook yourself. ")
            breakfast_personality = game_play_functions.choose_breakfast(what_breakfast)
            personality_type_status(personality_type_answers, breakfast_personality)
            print("\nProgress: " + user_status_functions.update_progress_bar(total_questions, 5))

        # If the user wakes up before 9:30, they will get all of the following quesitons

        sit_in_class = input("You made it to class! Where are you sitting? Type 'a' for right up front, "
                              "'b' for in the back, or 'c' for wherever your friends are. ")
        result_sit_in_class = game_play_functions.where_sit(sit_in_class)
        personality_type_status(personality_type_answers, result_sit_in_class)
        print("\nProgress: " + user_status_functions.update_progress_bar(total_questions, total_questions - 3))

        print("Now it's time for lunch and your friends are going to Crossroads so you meet them there. "
              "What are you getting?")
        lunch = input("Type 'a' for a burrito bowl, 'b' for a sandwich, or 'c' for a salad. ")
        lunch_personality = game_play_functions.pick_lunch(lunch)
        personality_type_status(personality_type_answers, lunch_personality)
        print("\nProgress: " + user_status_functions.update_progress_bar(total_questions, total_questions - 2))

        print("After lunch you have to go to work. You're a tour guide in the Office of Admission.")
        people_on_tour = random.randint(1, 10)
        print(f"There are {people_on_tour} families on the tour today!")
        work = input("How do you want to handle this tour with the other tour guides on your shift today? "
                      "Type 'a' give the tour with another guide, "
                      "'b' for let another tour guide give it and stay back, or 'c' for give it yourself. ")
        work_personality = game_play_functions.pick_work(work)
        personality_type_status(personality_type_answers, work_personality)
        print("\nProgress: " + user_status_functions.update_progress_bar(total_questions, total_questions - 1))

        print("You finished work, it's time to study! Which library are you going to?")
        library = input("Type 'a' for Dinand, 'b' for science, or 'c' for Rehm. ")
        library_personality = game_play_functions.pick_library(library)
        personality_type_status(personality_type_answers, library_personality)
        print("\nProgress: " + user_status_functions.update_progress_bar(total_questions, total_questions))

        print("\nGreat job studying! Time for bed, sleep well!")

        # This code is to break a tie, and to give multiple different options for questions, 
        # so that if there is still a tie after the user answers one of the questions, they can answer a different one.
        number_of_ties = 0
        while your_personality(personality_type_answers, "Bob", "Kevin", "Stuart") == False:
            if number_of_ties == 0:
                print("\nThere's a tie! Answer another question to break the tie.")
            else:
                print("\nThere's still a tie! Answer another question to break the tie.")
            new_tiebreaker = input("To pick your question, type 'a' for a math question, 'b' for a geography question, "
                                   "and 'c' if you're feeling lazy and don't want another question. ")
            validate_new_tiebreaker = input_validation_functions.multiple_choice_validation(new_tiebreaker)
            if validate_new_tiebreaker == "a":
                personality_type_status(personality_type_answers, "Kevin")
                math_question = input_validation_functions.math_question_validation()
                if math_question == 10:
                    print("That's correct!")
                else:
                    print(f"That is incorrect. You answered {math_question}, but the correct answer was 10.")
            elif validate_new_tiebreaker == "b":
                personality_type_status(personality_type_answers, "Bob")
                geography_question = input("What country has the largest surface area in the world? ")
                if geography_question.capitalize() == 'Russia':
                    print("That's correct!")
                else:
                    print(f"That's incorrect. You guessed {geography_question}, but the correct answer was Russia.")
            elif validate_new_tiebreaker == "c":
                personality_type_status(personality_type_answers, "Stuart")
            number_of_ties += 1

        users_personality = your_personality(personality_type_answers, "Bob", "Kevin", "Stuart")
       
        print(f"\nYou are most like {users_personality}")
        if users_personality == "Bob":
            print("Just like Bob, you love spending time with your friends. You're very optimistic and walk through " 
            "the world with a childlike wonder. Your closest friends would describe you as caring and supportive, " 
            "but sometimes your childlike heart can make you a little naive. ")
        elif users_personality == "Kevin":
            print("Just like Kevin, you're the Mom of the friend group. You're very organized and are a true go-getter. " 
            "You're a natural leader, but sometimes you can come off as a little bossy, but you're only bossy because " 
            "you care!")
        elif users_personality == "Stuart":
            print("Just like Stuart, you're very easy-going and mischevous. You have a great sense of humor and " 
            "are very fun-loving. However, sometimes you are a little too easy-going and could benefit from being " 
            "a little more organized.")
        print("\n" + test_if_player_wins(personality_type_answers, "Bob", "Kevin", "Stuart", validated_guess))