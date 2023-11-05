import streamlit as st

def main():
    st.title("Flames Game")
    
    name = st.text_input("Enter your name").lower().strip()
    crush = st.text_input("Enter your crush's name").lower().strip()
    submit_button = st.button("Submit")

    if submit_button:
        if name and crush:
            name_list = list_word(name)
            crush_list = list_word(crush)

            length_of_uncommon = find_length(name_list, crush_list)
            flame = flames(length_of_uncommon)
            output = check_condition(flame[0])

            st.write(f"Result: {output}")

            file_write(name, crush, output)

def list_word(name):
    name_list = []
    for i in name:
        name_list.append(i)
    return name_list

# Rest of your functions remain unchanged

if __name__ == '__main__':
    main()
