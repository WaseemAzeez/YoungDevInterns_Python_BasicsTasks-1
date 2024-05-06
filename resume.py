import streamlit as st

def main():
    st.title("My Digital Resume")

    # Personal Information section
    st.header("Personal Information")
    name = st.text_input("Name", "")
    email = st.text_input("Email", "")
    phone = st.text_input("Phone", "")

    # Education section
    st.header("Education")
    education = st.text_area("Education", "")

    # Work Experience section
    st.header("Work Experience")
    work_experience = st.text_area("Work Experience", "")

    # Skills section
    st.header("Skills")
    skills = st.text_area("Skills", "")

    # Projects section
    st.header("Projects")
    projects = st.text_area("Projects", "")

    # Render the resume
    st.subheader("Resume Preview")
    st.write(f"Name: {name}")
    st.write(f"Email: {email}")
    st.write(f"Phone: {phone}")
    st.write(f"Education:\n{education}")
    st.write(f"Work Experience:\n{work_experience}")
    st.write(f"Skills:\n{skills}")
    st.write(f"Projects:\n{projects}")

if __name__ == "__main__":
    main()
