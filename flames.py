def main():
    name = input("Enter your name: ").lower().strip()
    crush = input("Enter your crush's name: ").lower().strip()
    name_list = list_word(name)
    crush_list = list_word(crush)

    length_of_uncommon = find_length(name_list, crush_list)

    flame = flames(length_of_uncommon)
    output = check_condition(flame[0])
    print(output)

    file_write(name, crush, output)

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

    for i in common_words:
        name.remove(i)
        crush.remove(i)

    for i in repeating:
        if i in name and i in crush:
            name.remove(i)
            crush.remove(i)

    length = len(name) + len(crush)
    return length

def flames(value):
    flam = 'flames'
    flame = list(flam)
    while len(flame) > 1:
        if value > len(flame):
            difference = value - len(flame)
            while difference > len(flame):
                difference = difference - len(flame)
            new_flame = flame[difference:]
            flame.remove(flame[difference - 1])
            for i in flame:
                if i not in new_flame:
                    new_flame.append(i)
            flame = new_flame
        elif value == 0:
            return ['x']
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
    if flame.lower().strip() == 'f':
        return "FRIENDS"
    elif flame.lower().strip() == 'l':
        return "LOVERS"
    elif flame.lower().strip() == 'a':
        return "AFFECTION"
    elif flame.lower().strip() == 'm':
        return "MARRIAGE"
    elif flame.lower().strip() == 'e':
        return "ENEMY"
    elif flame.lower().strip() == 's':
        return "SIBLINGS"

def file_write(name, crush, output):
    with open("main.txt", "a") as file:
        file.write(f"{name},{crush},{output}\n")

if __name__ == '__main__':
    main()
