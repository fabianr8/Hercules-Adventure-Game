# You can use this workspace to write and submit your adventure game project.
import time
import random
import pycodestyle
berries = False

villains = ["Serverus the three-headed dog!!",
            "The Hideous Hades!!",
            "The Fifty-Headed Hydra!!"]
villain = random.choice(villains)


def print_pause(message):
    print(message)
    time.sleep(2)


def forrest():
    global berries
    choice = valid_input("\nEnter (1) to stay in the " +
                         "bright side of the forrest.\n" +
                         "Enter (2) to venture into the " +
                         "ominous dark-side.\n", ['1', '2'])
    if choice == '1':
        print_pause("\nYou were unable to find any berries and " +
                    "now you are feeling especially weak.")
        print_pause("\nYou get ambushed by " + villain)
    else:
        berries = True
        print_pause("\nYou manage to find some very satisfying berries " +
                    "you are immediately feeling courageous and strong " +
                    "you return to the lightside of the forrest ")
        print_pause("\nYou get ambushed by " + villain)


def battle():
    global berries
    global villains
    global villain
    choice = valid_input("\nEnter (1) to stay and fight.\n" +
                         "Enter (2) to run away.\n", ['1', '2'])
    if choice == '2':
        if berries:
            print_pause("\nYou have escaped back to field but "
                        + villain + " Catches up " +
                        "to you. \n\nYou are forced to " +
                        "fight and since you have the strength " +
                        "from the berries you win the battle!!")
            play_again()
        else:
            print_pause("\nYou have escaped back to the field but "
                        + villain + " Catches up to you and you are " +
                        "defeated!! \n\nGAME OVER!! ")
            play_again()
    elif choice == '1':
        if berries:
            print_pause("\nYou feel the power of the magical berries" +
                        " coursing through your body and are able to slay "
                        + villain + " \nYou have won the game!!!")
            play_again()
        else:
            print_pause("\nYou are hindered by your hunger and you are " +
                        "defeated by " + villain + " You have lost." +
                        "\n\nGAME OVER!! ")
            play_again()


def play_game():
    global berries
    global villains
    global villain
    while True:
        print("NEW GAMMEE HERE")
        berries = False
        villain = random.choice(villains)

        print_pause("Welcome Hercules! you are the mythical demi-god " +
                    "of ancient Greece! " +
                    "You are strong and courageously heroic!\n")
        print_pause("You are traversing a field and decide to " +
                    "rumage through a mystical forrest for " +
                    "berries, Yum! The forrest is clear and " +
                    "bright but inthe distance you spot " +
                    "some large juicy berries on " +
                    "the dark side of the forrest.\n")
        forrest()
        battle()


def play_again():
    choice = valid_input("Play again? [y|n]", ['y', 'n'])

    if choice == 'n':
        print('Thanks for playing! Goodbye!')
        exit(0)


def game():

    # Infinite loop.
    while True:
        # All logic to play.
        play_game()

        # The stop condition.
        play_again()


def valid_input(prompt, options):
    while True:
        option = input(prompt).lower()
        if option in options:
            return option
        print_pause(f'Sorry, the option "{option}" is invalid. Try again!')

# beginning of the game


if __name__ == '__main__':
    game()