
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from pypdf import PdfReader

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Smart Career Guidance System",
    page_icon="🎯",
    layout="wide"
)

# ============================================================
# TITLE
# ============================================================

st.title("🎯 Smart Career Guidance System Using AI")
st.write(
    "An AI-powered system for career prediction, skill-gap analysis, "
    "personalized roadmaps and career simulation."
)

st.divider()

# ============================================================
# CAREER DATASET
# ============================================================

data = {
    "Python": [
        9, 8, 7, 3, 2, 5, 8, 9,
        7, 6, 4, 8, 9, 3, 5
    ],

    "Java": [
        3, 4, 8, 2, 1, 9, 2, 3,
        7, 8, 6, 4, 3, 7, 9
    ],

    "SQL": [
        8, 7, 6, 2, 2, 5, 7, 8,
        6, 7, 5, 6, 8, 3, 5
    ],

    "ML": [
        9, 9, 7, 1, 1, 3, 8, 9,
        7, 6, 2, 8, 9, 1, 3
    ],

    "Web": [
        3, 4, 6, 9, 8, 7, 3, 2,
        7, 8, 9, 4, 2, 8, 7
    ],

    "CyberSecurity": [
        5, 4, 3, 7, 6, 3, 5, 4,
        3, 2, 8, 5, 4, 9, 8
    ],

    "DataAnalysis": [
        9, 8, 7, 2, 2, 5, 8, 9,
        7, 6, 3, 8, 9, 2, 4
    ],

    "Career": [
        "Data Scientist",
        "AI Engineer",
        "Software Developer",
        "Web Developer",
        "Cyber Security Analyst",
        "Software Developer",
        "Data Scientist",
        "AI Engineer",
        "Software Developer",
        "Software Developer",
        "Cyber Security Analyst",
        "Data Scientist",
        "AI Engineer",
        "Cyber Security Analyst",
        "Software Developer"
    ]
}

df = pd.DataFrame(data)

# ============================================================
# TRAIN MACHINE LEARNING MODEL
# ============================================================

features = [
    "Python",
    "Java",
    "SQL",
    "ML",
    "Web",
    "CyberSecurity",
    "DataAnalysis"
]

X = df[features]
y = df["Career"]

encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X, y_encoded)

# ============================================================
# CAREER REQUIREMENTS
# ============================================================

career_requirements = {

    "Data Scientist": {
        "Python": 8,
        "SQL": 7,
        "ML": 8,
        "DataAnalysis": 9
    },

    "AI Engineer": {
        "Python": 9,
        "ML": 9,
        "SQL": 6,
        "DataAnalysis": 7
    },

    "Software Developer": {
        "Python": 6,
        "Java": 8,
        "SQL": 6,
        "Web": 6
    },

    "Web Developer": {
        "Python": 4,
        "Java": 5,
        "Web": 9,
        "SQL": 5
    },

    "Cyber Security Analyst": {
        "Python": 6,
        "CyberSecurity": 9,
        "SQL": 5
    }
}

# ============================================================
# PROJECT RECOMMENDATIONS
# ============================================================

project_recommendations = {

    "Data Scientist": [
        "Customer Churn Prediction",
        "House Price Prediction",
        "Sales Forecasting",
        "Movie Recommendation System"
    ],

    "AI Engineer": [
        "AI Chatbot",
        "Image Classification System",
        "Document Question Answering System",
        "AI Recommendation System"
    ],

    "Software Developer": [
        "College Management System",
        "Expense Tracker",
        "Online Library System",
        "Student Management System"
    ],

    "Web Developer": [
        "E-Commerce Website",
        "Portfolio Website",
        "Online Learning Platform",
        "College Event Website"
    ],

    "Cyber Security Analyst": [
        "Phishing Detection System",
        "Network Intrusion Detection",
        "Password Security Analyzer",
        "Malware Detection Prototype"
    ]
}

# ============================================================
# ROADMAP
# ============================================================

roadmaps = {

    "Data Scientist": [
        "Python",
        "NumPy and Pandas",
        "Statistics",
        "SQL",
        "Machine Learning",
        "Data Visualization",
        "Deep Learning",
        "Build Data Science Projects"
    ],

    "AI Engineer": [
        "Python",
        "NumPy and Pandas",
        "Machine Learning",
        "Deep Learning",
        "Natural Language Processing",
        "Generative AI",
        "RAG Systems",
        "Build AI Projects"
    ],

    "Software Developer": [
        "Programming Fundamentals",
        "Java/Python",
        "Data Structures",
        "Algorithms",
        "SQL",
        "Object-Oriented Programming",
        "Software Development",
        "Build Applications"
    ],

    "Web Developer": [
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "Backend Development",
        "APIs",
        "Databases",
        "Build Full-Stack Projects"
    ],

    "Cyber Security Analyst": [
        "Computer Networks",
        "Linux",
        "Python",
        "Cyber Security Fundamentals",
        "Authentication",
        "Network Security",
        "Security Monitoring",
        "Build Security Projects"
    ]
}

# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("📌 Navigation")

page = st.sidebar.radio(
    "Choose Module",
    [
        "Student Profile",
        "Career Prediction",
        "Skill Gap",
        "Career Roadmap",
        "Project Recommendations",
        "What-If Simulator",
        "Resume Analyzer",
        "AI Career Assistant"
    ]
)

# ============================================================
# SESSION STATE
# ============================================================

if "career" not in st.session_state:
    st.session_state.career = None

if "scores" not in st.session_state:
    st.session_state.scores = {}

if "skills" not in st.session_state:
    st.session_state.skills = {}

# ============================================================
# STUDENT PROFILE
# ============================================================

if page == "Student Profile":

    st.header("👨‍🎓 Student Profile")

    name = st.text_input("Student Name")

    branch = st.selectbox(
        "Branch",
        [
            "Computer Science Engineering",
            "Information Technology",
            "Electronics and Communication",
            "Electrical Engineering",
            "Mechanical Engineering",
            "Civil Engineering"
        ]
    )

    year = st.selectbox(
        "Year",
        [
            "1st Year",
            "2nd Year",
            "3rd Year",
            "4th Year"
        ]
    )

    st.subheader("🧠 Rate Your Skills")

    python = st.slider("Python", 0, 10, 5)
    java = st.slider("Java", 0, 10, 5)
    sql = st.slider("SQL", 0, 10, 5)
    ml = st.slider("Machine Learning", 0, 10, 5)
    web = st.slider("Web Development", 0, 10, 5)
    cyber = st.slider("Cyber Security", 0, 10, 5)
    data_analysis = st.slider("Data Analysis", 0, 10, 5)

    if st.button("💾 Save Profile"):

        st.session_state.name = name
        st.session_state.branch = branch
        st.session_state.year = year

        st.session_state.skills = {
            "Python": python,
            "Java": java,
            "SQL": sql,
            "ML": ml,
            "Web": web,
            "CyberSecurity": cyber,
            "DataAnalysis": data_analysis
        }

        st.success("Profile saved successfully!")

# ============================================================
# CAREER PREDICTION
# ============================================================

elif page == "Career Prediction":

    st.header("🤖 AI Career Prediction")

    if not st.session_state.skills:

        st.warning(
            "Please complete your Student Profile first."
        )

    else:

        student = pd.DataFrame(
            [st.session_state.skills]
        )

        prediction = model.predict(student)

        career = encoder.inverse_transform(
            prediction
        )[0]

        probabilities = model.predict_proba(student)[0]

        ranking = pd.DataFrame({
            "Career": encoder.classes_,
            "Compatibility": [
                round(p * 100, 2)
                for p in probabilities
            ]
        })

        ranking = ranking.sort_values(
            "Compatibility",
            ascending=False
        )

        st.session_state.career = career

        st.success(
            f"🎯 Recommended Career: {career}"
        )

        st.metric(
            "Top Career Compatibility",
            f"{ranking.iloc[0]['Compatibility']}%"
        )

        st.subheader("📊 Career Ranking")

        st.bar_chart(
            ranking.set_index("Career")
        )

        st.dataframe(
            ranking,
            use_container_width=True
        )

# ============================================================
# SKILL GAP
# ============================================================

elif page == "Skill Gap":

    st.header("🔍 AI Skill Gap Analysis")

    career = st.session_state.career

    if not career:

        st.warning(
            "Please run Career Prediction first."
        )

    else:

        requirements = career_requirements[career]
        skills = st.session_state.skills

        gap_data = []

        for skill, required in requirements.items():

            current = skills.get(skill, 0)

            gap = max(
                required - current,
                0
            )

            gap_data.append({
                "Skill": skill,
                "Current Level": current,
                "Required Level": required,
                "Skill Gap": gap
            })

        gap_df = pd.DataFrame(gap_data)

        st.dataframe(
            gap_df,
            use_container_width=True
        )

        st.subheader("📈 Skill Improvement")

        for row in gap_data:

            skill = row["Skill"]
            current = row["Current Level"]
            required = row["Required Level"]

            st.write(
                f"**{skill}: {current}/10 → {required}/10**"
            )

            st.progress(
                min(current / 10, 1.0)
            )

# ============================================================
# CAREER ROADMAP
# ============================================================

elif page == "Career Roadmap":

    st.header("🗺️ Adaptive Career Roadmap")

    career = st.session_state.career

    if not career:

        st.warning(
            "Please run Career Prediction first."
        )

    else:

        st.write(
            f"Career Target: **{career}**"
        )

        roadmap = roadmaps[career]

        for i, step in enumerate(
            roadmap,
            start=1
        ):

            completed = st.checkbox(
                f"Step {i}: {step}",
                key=f"roadmap_{i}"
            )

            if completed:
                st.success(
                    f"{step} completed!"
                )

# ============================================================
# PROJECT RECOMMENDATIONS
# ============================================================

elif page == "Project Recommendations":

    st.header("💡 AI Project Recommendation Engine")

    career = st.session_state.career

    if not career:

        st.warning(
            "Please run Career Prediction first."
        )

    else:

        st.write(
            f"Recommended projects for **{career}**:"
        )

        projects = project_recommendations[career]

        for i, project in enumerate(
            projects,
            start=1
        ):

            st.info(
                f"Project {i}: {project}"
            )

# ============================================================
# WHAT-IF SIMULATOR
# ============================================================

elif page == "What-If Simulator":

    st.header("🔄 What-If Career Simulator")

    st.write(
        "Change your skill levels and see how "
        "your career compatibility changes."
    )

    if not st.session_state.skills:

        st.warning(
            "Please save your Student Profile first."
        )

    else:

        simulated = {}

        for skill in features:

            simulated[skill] = st.slider(
                f"{skill} - Simulated Level",
                0,
                10,
                int(st.session_state.skills[skill])
            )

        if st.button("🔮 Simulate Career"):

            simulated_df = pd.DataFrame(
                [simulated]
            )

            probabilities = model.predict_proba(
                simulated_df
            )[0]

            results = pd.DataFrame({
                "Career": encoder.classes_,
                "Projected Compatibility": [
                    round(p * 100, 2)
                    for p in probabilities
                ]
            })

            results = results.sort_values(
                "Projected Compatibility",
                ascending=False
            )

            st.subheader(
                "🔮 Projected Career Compatibility"
            )

            st.dataframe(
                results,
                use_container_width=True
            )

            st.success(
                f"Potential top career: "
                f"{results.iloc[0]['Career']}"
            )

# ============================================================
# RESUME ANALYZER
# ============================================================

elif page == "Resume Analyzer":

    st.header("📄 AI Resume Skill Analyzer")

    uploaded_file = st.file_uploader(
        "Upload your resume PDF",
        type=["pdf"]
    )

    if uploaded_file:

        reader = PdfReader(uploaded_file)

        resume_text = ""

        for page_data in reader.pages:

            text = page_data.extract_text()

            if text:
                resume_text += text + "\n"

        st.subheader("📋 Extracted Resume Text")

        st.text_area(
            "Resume",
            resume_text,
            height=250
        )

        skill_keywords = {
            "Python": ["python"],
            "Java": ["java"],
            "SQL": ["sql", "mysql"],
            "ML": [
                "machine learning",
                "scikit-learn",
                "sklearn"
            ],
            "Web": [
                "html",
                "css",
                "javascript",
                "react",
                "web development"
            ],
            "CyberSecurity": [
                "cyber security",
                "cybersecurity",
                "network security"
            ],
            "DataAnalysis": [
                "data analysis",
                "pandas",
                "numpy",
                "data visualization"
            ]
        }

        detected = []

        resume_lower = resume_text.lower()

        for skill, keywords in skill_keywords.items():

            for keyword in keywords:

                if keyword in resume_lower:

                    detected.append(skill)
                    break

        st.subheader("🔎 Detected Skills")

        if detected:

            for skill in detected:
                st.success(f"✓ {skill}")

        else:

            st.warning(
                "No predefined skills detected."
            )

# ============================================================
# AI CAREER ASSISTANT
# ============================================================

elif page == "AI Career Assistant":

    st.header("💬 Personalized Career Assistant")

    career = st.session_state.career

    if career:

        st.info(
            f"Your current recommended career is: **{career}**"
        )

    question = st.text_input(
        "Ask a career question"
    )

    if st.button("Ask Assistant"):

        if not question:

            st.warning(
                "Please enter a question."
            )

        else:

            q = question.lower()

            if "next" in q or "learn" in q:

                if career:

                    roadmap = roadmaps[career]

                    st.write(
                        f"Based on your target career "
                        f"**{career}**, focus on:"
                    )

                    for item in roadmap[:3]:

                        st.write(
                            f"➡️ {item}"
                        )

                else:

                    st.write(
                        "Complete your career assessment "
                        "first."
                    )

            elif "project" in q:

                if career:

                    st.write(
                        "Recommended projects:"
                    )

                    for project in project_recommendations[career]:

                        st.write(
                            f"💡 {project}"
                        )

            elif "career" in q:

                if career:

                    st.write(
                        f"Your current AI-recommended "
                        f"career is **{career}**."
                    )

                else:

                    st.write(
                        "Complete the career prediction "
                        "module first."
                    )

            else:

                st.write(
                    "I can help you with careers, "
                    "skills, projects and learning roadmaps."
                )

# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Smart Career Guidance System Using AI | CSE Project Prototype"
)
