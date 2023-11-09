import streamlit as st

def main():
    st.title("Flames Game")
    name = st.text_input("Enter your name: ").lower().strip()
    crush = st.text_input("Enter your crush's name: ").lower().strip()
    
    if st.button("Submit"):
        output = calculate_flames(name, crush)
        st.write(f"Result: {output}")
        file_write(name, crush, output)

def list_word(name):
    return list(name)

def find_length(name, crush):
    name_set = set(name)
    crush_set = set(crush)
    uncommon_characters = len(name_set.symmetric_difference(crush_set))
    return uncommon_characters

def flames(value):
    flame = list("flames")
    while len(flame) > 1:
        index = value % len(flame) - 1
        flame.pop(index)
    return flame[0]

def check_condition(flame):
    conditions = {
        'f': "FRIENDS",
        'l': "LOVERS",
        'a': "AFFECTION",
        'm': "MARRIAGE",
        'e': "ENEMY",
        's': "SIBLINGS"
    }
    return conditions.get(flame.lower().strip(), "Invalid Result")

def file_write(name, crush, output):
    with open("main.txt", "a") as file:
        file.write(f"{name},{crush},{output}\n")

def calculate_flames(name, crush):
    name_list = list_word(name)
    crush_list = list_word(crush)
    length_of_uncommon = find_length(name_list, crush_list)
    flame = flames(length_of_uncommon)
    output = check_condition(flame)
    return output

if __name__ == '__main__':
    main()
