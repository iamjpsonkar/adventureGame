import time
import sys
import random
items = []
baddie_badbad = random.choice(["frogman", "elfpen", "cartman"])


def fightrun_function():
    response = valid_input("Please enter 1 or 2.\n", "1", "2")
    if "1" in response:
        opt_fight()
    elif "2" in response:
        opt_run()
    else:
        fightrun_function()
    option_house()


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if response == option1:
            return response
        elif response == option2:
            return response
        else:
            print_pause("Sorry, I don't understand.")
    return response


def intro_intro():
    print_pause("You find yourself standing in an open field,"
                "filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a wicked creature is somewhere "
                "around here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty"
                "(but not very effective) dagger.\n\n")
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    one_two()


def play_again():
    response = valid_input("Would you like to play again?"
                           " Please say 'yes' or 'no'.\n", "yes", "no")
    if "no" in response:
        print_pause("OK, goodbye!")
        sys.exit(1)
    elif "yes" in response:
        items.remove("Magical Sword")
        intro_intro()


def opt_run():
    print_pause("You run back into the field. Luckily,"
                "you don't seem to have been followed.")
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    one_two()


def opt_fight():
    if "Magical Sword" in items:
        print_pause("As the " + baddie_badbad + " moves to attack, "
                    " you unsheath your new sword.")
        print_pause("The Sword of Ogoroth shines brightly in your"
                    " hand as you brace yourself for the attack.")
        print_pause("But the " + baddie_badbad + " takes one look at"
                    " your shiny new toy and runs away!")
        print_pause("You have rid the town of the " + baddie_badbad +
                    " You are victorious!")
        play_again()
    else:
        print_pause("You do your best...")
        print_pause("but your dagger is no match for the wicked " +
                    baddie_badbad)
        print_pause("You have been defeated!")
        play_again()


def opt_peer():
    print_pause("You peer cautiously into the cave.")
    print_pause("You've been here before, and gotten all the good stuff."
                " It's just an empty cave now.")
    print_pause("You walk back out to the field.\n\n")
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    one_two()


def option_house():
    baddie_badbad = random.choice(["frogman", "elfpen", "cartman"])
    if "Magical Sword" in items:
        print_pause("You approach the door of the house.")
        print_pause("You are about to knock when the door opens"
                    " and out steps a " + baddie_badbad)
        print_pause("Eep! This is the " + baddie_badbad + "house!")
        print_pause("The " + baddie_badbad + "attacks you!")
        print_pause("Would you like to (1) fight or (2) run away?")
        fightrun_function()

    else:
        print_pause("You approach the door of the house.")
        print_pause("You are about to knock when the door opens"
                    " and out steps a " + baddie_badbad)
        print_pause("Eep! This is the " + baddie_badbad + " house!")
        print_pause("The " + baddie_badbad + " attacks you!")
        print_pause("You feel a bit under-prepared for this, "
                    "what with only having a tiny dagger.")
        print_pause("Would you like to (1) fight or (2) run away?")
        fightrun_function()


def option_cave():
    if "Magical Sword" in items:
        opt_peer()

    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        items.append("Magical Sword")
        print_pause("You discard your silly old dagger and take the"
                    " sword with you.")
        print_pause("You walk back out to the field.\n\n ")
        print_pause("Enter 1 to knock on the door of the house.\n" +
                    " Enter 2 to peer into the cave.")
        print_pause("What would you like to do?")
        one_two()


def one_two():
    while True:
        response = valid_input("Please enter 1 or 2.\n", "1", "2")
        if response == "1":
            option_house()
            return
        elif response == "2":
            option_cave()
            return
        else:
            print_pause("Sorry I don't understand")
        one_two()

intro_intro()
