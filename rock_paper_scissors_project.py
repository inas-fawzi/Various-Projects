# Introduction to programming
# Final Project: Rock Paper Scissors Game
# Student ID and name: 1959334 Inas Fawzi

import random


def best_of_r(r):
    r_user = 0
    r_comp = 0
    while r > 0:
        rps = ["rock", "paper", "scissors"]
        comp = random.choice(rps)
        user = input("Do you play rock, paper or scissors?")
        while (user.lower() is False) or (user.lower() != "rock" and user.lower() != "paper" and user.lower() != "scissors"):
            print("You can only choose rock, paper or scissors. I knew you were bluffing, you don't even know how to play!")
            user = input("Do you play rock, paper or scissors?")
        result = play_round(user, comp)
        if result == "win":
            r_user = r_user + 1
            r_comp = r_comp + 0
        elif result == "lose":
            r_user = r_user + 0
            r_comp = r_comp + 1
        elif result == "tie":
            r_user = r_user + 0
            r_comp = r_comp + 0
        r = r - 1
    if r_user == r_comp:
        result_r = "tie"
    elif r_user > r_comp:
        result_r = "win"
    elif r_user < r_comp:
        result_r = "lose"
    return result_r


def play_round(user, comp):
    if user.lower() == "rock":
        if comp == "rock":
            print("You picked ", user, "and I also picked ", comp, ". Looks like we tied for this one.")
            result = "tie"
        elif comp == "scissors":
            print("You picked ", user, "and I picked ", comp, ". You won this time, but it was just luck >:O")
            result = "win"
        elif comp == "paper":
            print("You picked ", user, "and I picked ", comp, ". I won, as expected!")
            result = "lose"
    elif user.lower() == "paper":
        if comp == "rock":
            print("You picked ", user, "and I picked ", comp, ". You won this time, but it was just luck >:O")
            result = "win"
        elif comp == "scissors":
            print("You picked ", user, "and I picked ", comp, ". I won, as expected!")
            result = "lose"
        elif comp == "paper":
            print("You picked ", user, "and I also picked ", comp, ". Looks like we tied for this one.")
            result = "tie"
    elif user.lower() == "scissors":
        if comp == "rock":
            print("You picked ", user, "and I picked ", comp, ". I won, as expected!")
            result = "lose"
        elif comp == "scissors":
            print("You picked ", user, "and I also picked ", comp, ". Looks like we tied for this one.")
            result = "tie"
        elif comp == "paper":
            print("You picked ", user, "and I picked ", comp, ". You won this time, but it was just luck >:O")
            result = "win"
    return result


def main():
    # Introduction
    name = input("Hello there! What's your name?")
    print("....You're ", name, "?")
    print("I heard you've been going around saying you can beat anyone in a rock paper scissors game.")
    print("There's no way you could beat me though. (-_-)")
    print("Dare to challenge me?")
    choice = input("Type y to challenge, or n to run away")
    while choice != "n" and choice != "N" and choice != "y" and choice != "Y":
        choice = input("Hey, it's a simple question! You can answer y to challenge me, or n to run away.")
    if choice.lower() == "n":
        print("Wise choice, you would never beat me. Run along!")
    while choice.lower() == "y":
        print("Well well, may the best player win then!")
        print("Should we do a best of 3 match, best of 5 match or a single match?")
        match = input("Type 1 for a single match, 3 for a best of three match, or 5 for a best of five match.")
        while match != "1" and match != "3" and match != "5":
            print("I'm letting you choose, but it has to be best of three, five or a single match only! >:O")
            match = input("Type 1 for a single match, type 3 for a best of three match, or type 5 for a best of five match.")
        if match == "1":
            print("Single match! You have one chance to beat me!")
            rps = ["rock", "paper", "scissors"]
            comp = random.choice(rps)
            user = input("Do you play rock, paper or scissors?")
            while (user.lower() is False) or (user.lower() != "rock" and user.lower() != "paper" and user.lower() != "scissors"):
                print("You can only choose rock, paper or scissors. I knew you were bluffing, you don't even know how to play!")
                user = input("Do you play rock, paper or scissors?")
            result = play_round(user, comp)
            print("This game you ", result, ". Do you dare to challenge me again?")
        elif match == "3":
            print("Best of three match! Let's see who wins!")
            r = 3
            result_r = best_of_r(r)
            print("This game you ", result_r, ". Do you dare to challenge me again?")
        elif match == "5":
            print("Best of five match! Let's see who wins!")
            r = 5
            result_r = best_of_r(r)
            print("This game you ", result_r, ". Do you dare to challenge me again?")
        reply = input("Type yes to challenge me again, and no to stop playing.")
        while (reply.lower() is False) or (reply.lower() != "yes" and reply.lower() != "no"):
            reply = input("Hey, it's a yes or no question! Do you want to challenge me again; yes or no?")
        if reply.lower() == "yes":
            choice = "y"
        elif reply.lower() == "no":
            choice = "n"


if __name__ == '__main__':
    main()
