import streamlit as st

st.title("🎓 GPA Calculator")

subjects = st.number_input("Number of Subjects", min_value=1)

grades = []
for i in range(subjects):
    grade = st.number_input(f"Grade for Subject {i+1}", min_value=0.0, max_value=10.0)
    grades.append(grade)

if st.button("Calculate GPA"):
    if subjects > 0:
        gpa = sum(grades) / subjects
        st.success(f"Your GPA is: {gpa:.2f}")