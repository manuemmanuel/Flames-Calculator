from pyfiglet import Figlet
from tabulate import tabulate
from cowsay import get_output_string

def main():
    figlet("FLAMES", "block")
    key = "y"
    while key == "y":
        name = input("Enter your name: ").lower().strip()
        crush = input("Enter your crush's name: ").lower().strip()
        name_list = list_word(name)
        crush_list = list_word(crush)

        length_of_uncommon = find_length(name_list, crush_list)

        flame = flames(length_of_uncommon)
        output = check_condition(flame[0])
        animate(output)

        file_write(name.capitalize(), crush.capitalize(), output)
        history = input("Do you want to view your history ? (y/n) ").lower().strip()
        if history == "y":
            history_list = file_read()
            if len(history_list) > 0:
                print_table(history_list)
            else:
                print("No History To Be Diplayed !!")
        key = input("Do you want to check again ? (y/n) ").lower().strip()

    print("\nThank you for using the Flames Calculator.")
    figlet("GOOD BYE !!", "graceful")


def list_word(name):
    name_list = []

    for i in name:
        name_list.append(i)

    return name_list


def find_length(name, crush):
    common_words = []
    repeating = []
    if len(name) > len(crush):
        for i in crush:
            for j in name:
                if i == j:
                    common_words.append(i)
                    break
    else:
        for i in name:
            for j in crush:
                if i == j:
                    common_words.append(i)
                    break

    for i in common_words:
        if common_words.count(i) > 1:
            repeating.append(i)
            common_words.remove(i)

    for i in repeating:
        if i in name and i in crush:
            name.remove(i)
            crush.remove(i)

    length = len(name) + len(crush)
    return length


def flames(value):
    flame = list("flames")
    new_flame = []

    while len(flame) > 1:
        if value > len(flame):
            difference = value - len(flame)
            difference -= 1

            while difference >= len(flame):
                difference -= len(flame)

            new_flame = flame[difference:]
            flame.remove(flame[difference - 1])

            for i in flame:
                if i not in new_flame:
                    new_flame.append(i)

            flame = new_flame
        elif value == len(flame):
            flame.remove(flame[-1])
        else:
            while value < len(flame):
                new_flame = flame[value:]
                flame.remove(flame[value - 1])

                for i in flame:
                    if i not in new_flame:
                        new_flame.append(i)

                flame = new_flame

    return flame


def check_condition(flame):
    if flame.lower().strip() == "f":
        return "FRIENDS"
    elif flame.lower().strip() == "l":
        return "LOVERS"
    elif flame.lower().strip() == "a":
        return "AFFECTION"
    elif flame.lower().strip() == "m":
        return "MARRIAGE"
    elif flame.lower().strip() == "e":
        return "ENEMY"
    elif flame.lower().strip() == "s":
        return "SIBLINGS"


def file_write(name, crush, output):
    with open("main.txt", "a") as file:
        file.write(f"{name},{crush},{output}\n")


def figlet(value, fonts):
    f = Figlet(font=fonts)
    print(f.renderText(value))


def file_read():
    with open("main.txt", "r") as file:
        content = file.readlines()
        history_list = []
        for i in content:
            term = i.strip().split(",")
            history_list.append(term)

        return history_list


def print_table(history_list):
    print(
        tabulate(
            history_list, headers=["Your Name", "Crush's Name", "Result"], tablefmt="pretty"
        )
    )


def animate(output):
    if output.lower() == "friends":
        print(
            get_output_string("milk", f"Your are just\n{output}\nhaha...friendzoned !!")
        )
    elif output.lower() == "lovers":
        print(
            get_output_string(
                "cow",
                f"You are \n{output}\nRelationships are a lot like algebra. You look at your X and wonder Y. hahaha....",
            )
        )
    elif output.lower() == "marriage":
        print(
            get_output_string(
                "turtle",
                f"The result is \n{output}\nsome random advice for you..\nMarriage is when a man and woman become one. The trouble starts when they try to decide which one.So better think twice ...\nhaha...",
            )
        )
    elif output.lower() == "affection":
        print(
            get_output_string(
                "octopus",
                f"Just {output}\nWhat did one octopus say to the other octopus?\n'Want to hold my hand? I've got eight to spare!'\nhehe...I know I'm funny .. Thankss..",
            )
        )

    elif output.lower() == "enemy":
        print(
            get_output_string(
                "trex",
                f"Ohh Ohh !! You are\n{output}\nOhh Ohh the misery\nEverybody want to be my Enemy .. \n Spare the Sympathy ..Everybody want  to be my enemy ... yeahhh",
            )
        )
    elif output.lower() == "siblings":
        print(
            get_output_string(
                "beavis",
                f"You are just \n{output}\n which implies that you are one of the sore losers in this small world ... \nonce again best of luck finding that person",
            )
        )


if __name__ == "__main__":
    main()
