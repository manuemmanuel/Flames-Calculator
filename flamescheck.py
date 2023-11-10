import streamlit as st

def main():
    st.title("Flames Game")

    name = st.text_input("Enter your Name: ").lower().strip()
    crush = st.text_input("Enter your Crush's name: ").lower().strip()

    if st.button("Submit"):
        name_list = list_word(name)
        crush_list = list_word(crush)
        length_of_uncommon = find_length(name_list, crush_list)
        flame_result = flames(length_of_uncommon)
        output = check_condition(flame_result[0])

        st.write(f"Result: {output}")

        file_write(name, crush, output)

def list_word(word):
    return list(word)

def find_length(name, crush):
    common_words = set(name) & set(crush)
    repeating = [i for i in common_words if name.count(i) > 1]
    
    for i in repeating:
        name.remove(i)
        crush.remove(i)
    
    length = len(name) + len(crush)
    return length

def flames(value):
    flame = list('flames')
    while len(flame) > 1:
        if value > len(flame):
            difference = value - len(flame)
            new_flame = flame[difference:] + flame[:difference-1]
            flame = new_flame
        elif value == 0:
            return ['x']
        elif value == len(flame):
            flame.pop()
        else:
            new_flame = flame[value:] + flame[:value-1]
            flame = new_flame
    return flame

def check_condition(flame):
    conditions = {'f': "FRIENDS", 'l': "LOVERS", 'a': "AFFECTION", 'm': "MARRIAGE", 'e': "ENEMY", 's': "SIBLINGS"}
    return conditions.get(flame.lower().strip(), "Invalid")

def file_write(name, crush, output):
    with open("main.txt", "a") as file:
        file.write(f"{name},{crush},{output}\n")

if __name__ == '__main__':
    main()
