import streamlit as st
import requests

def calculate_relationship(name_one, name_two):
    count = 0
    num = len(name_one) + len(name_two)
    for i in range(len(name_one)):
        for j in range(len(name_two)):
            if name_one[i] == name_two[j]:
                count += 1
                name_two = name_two[:j] + '0' + name_two[j + 1:]
    number = num - 2 * count

    flames = ['f', 'l', 'a', 'm', 'e', 's']
    n = 0
    while len(flames) > 1:
        n = (n + number - 1) % len(flames)
        flames.pop(n)
    result = flames[0]

    return result


st.title("FLAMES Relationship Calculator")

name_one = st.text_input("Enter Name One:")
name_two = st.text_input("Enter Name Two:")
result = ""

if st.button("Calculate"):
    result_code = calculate_relationship(name_one.lower(), name_two.lower())
    if result_code == 'f':
        result = "Friends"
    elif result_code == 'l':
        result = "Lovers"
    elif result_code == 'a':
        result = "Affection"
    elif result_code == 'm':
        result = "Marriage"
    elif result_code == 'e':
        result = "Enemies"
    elif result_code == 's':
        result = "Siblings"

    st.write(f"Result: {result}")

    github_token = "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"  
    repo_owner = "manuemmanuel" 
    repo_name = "Flames-Calculator" 
    file_path = "result.txt"

  
    content = f"Name One: {name_one}\nName Two: {name_two}\nResult: {result}"
    response = requests.put(
        f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}",
        headers={"Authorization": f"Bearer {github_token}"},
        json={
            "message": "Update result.txt",
            "content": content.encode("base64").decode("utf-8"),
            "sha": None
        }
    )

    if response.status_code == 200:
        st.write("Data saved successfully!")
    else:
        st.write("Failed to save data. Please check your GitHub token and repository information.")
