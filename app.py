import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="My Engineering Degree OS",
    page_icon="🎓",
    layout="wide"
)

# Load CSV files
semesters = pd.read_csv("data/semesters.csv")
courses = pd.read_csv("data/courses.csv")
calendar = pd.read_csv("data/academic_calendar.csv")
assessments = pd.read_csv("data/assessments.csv")
scores = pd.read_csv("data/scores.csv")

# Title
st.title("🎓 MY ENGINEERING DEGREE OS")
st.write("Your Engineering Degree Dashboard")

# Sidebar
menu = st.sidebar.selectbox(
    "Select Section",
    ["Dashboard", "Syllabus", "Calendar",
     "Assessments", "Scores"]
)

# Dashboard
if menu == "Dashboard":
    st.header("Student Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Semesters", 8)
    col2.metric("Total Subjects", len(courses))
    col3.metric("Total Assessments", len(assessments))

    st.subheader("Semester Details")
    st.dataframe(semesters)

# Syllabus
elif menu == "Syllabus":
    st.header("Semester-wise Syllabus")

    sem = st.selectbox(
        "Choose Semester", range(1, 9)
    )

    data = courses[courses["semester"] == sem]
    st.dataframe(data)

# Calendar
elif menu == "Calendar":
    st.header("Academic Calendar")
    st.dataframe(calendar)

# Assessments
elif menu == "Assessments":
    st.header("Assessments")
    st.dataframe(assessments)

# Scores
elif menu == "Scores":
    st.header("Student Scorecard")
    st.dataframe(scores)

    total = scores["marks_obtained"].sum()
    maximum = scores["max_marks"].sum()

    st.metric(
        "Overall Percentage",
        f"{total / maximum * 100:.2f}%"
    )