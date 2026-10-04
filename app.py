
import html
import streamlit as st

from graph import generate_learning_path
from data import SKILLS, LEARNING_MATERIALS


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="LearnGraph AI",
    page_icon="🎓",
    layout="wide"
)


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>
.stApp {
    background-color: #0b1020;
    color: #ffffff;
}

.main-title {
    font-size: 48px;
    font-weight: 800;
    text-align: center;
    color: #a855f7;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #94a3b8;
    font-size: 18px;
    margin-bottom: 40px;
}

.section-title {
    color: #22d3ee;
    font-size: 24px;
    font-weight: 700;
}

.roadmap-card {
    background: linear-gradient(135deg, #111827, #1e1b4b);
    padding: 25px;
    border-radius: 18px;
    margin: 16px 0;
    border: 1px solid #4c1d95;
    box-shadow: 0 0 20px rgba(139, 92, 246, 0.15);
}

.skill-title {
    font-size: 28px;
    font-weight: 700;
    color: #c084fc;
}

.goal-card {
    background: linear-gradient(135deg, #164e63, #1e1b4b);
    padding: 25px;
    border-radius: 18px;
    margin-top: 30px;
    border: 1px solid #22d3ee;
}

.footer {
    text-align: center;
    color: #64748b;
    margin-top: 50px;
    padding: 20px;
}

.stButton > button {
    background: linear-gradient(90deg, #7c3aed, #0891b2);
    color: white;
    border: none;
    border-radius: 10px;
    font-weight: 700;
    padding: 12px;
}

.stButton > button:hover {
    border: 1px solid #22d3ee;
    color: white;
}

[data-testid="stExpander"] {
    border: 1px solid #334155;
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown(
    '<div class="main-title">🎓 LearnGraph AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Personalized Learning Roadmap using Knowledge Graphs'
    '</div>',
    unsafe_allow_html=True
)


# --------------------------------------------------
# INPUT SECTION
# --------------------------------------------------

st.markdown(
    '<div class="section-title">'
    '🎯 Build Your Learning Path'
    '</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    current_skill = st.selectbox(
        "What do you already know?",
        SKILLS,
        index=0
    )

with col2:
    target_skill = st.selectbox(
        "What do you want to learn?",
        SKILLS,
        index=1
    )


# --------------------------------------------------
# GENERATE ROADMAP
# --------------------------------------------------

if st.button(
    "🚀 Generate My Roadmap",
    use_container_width=True
):

    if current_skill == target_skill:
        st.warning(
            "Please choose different current and target skills."
        )

    else:
        try:
            learning_path = generate_learning_path(
                current_skill,
                target_skill
            )

        except (ValueError, KeyError) as error:
            st.error(f"Please check your learning data: {error}")
            learning_path = []

        if not learning_path:
            st.error(
                "No learning path exists between these skills. "
                "Check the prerequisite relationships in data.py."
            )

        else:
            st.markdown("## 🗺️ Your Personalized Roadmap")

            total_hours = 0

            for index, skill in enumerate(learning_path):

                material = LEARNING_MATERIALS.get(skill, {})

                # Ensure material is always a dictionary
                if not isinstance(material, dict):
                    material = {}

                description = material.get(
                    "description",
                    f"Learn the fundamentals of {skill}."
                )

                topics = material.get("topics", [])
                resources = material.get("resources", [])
                projects = material.get("projects", [])
                hours = material.get("hours", 0)

                # Validate collection types
                if not isinstance(topics, list):
                    topics = []

                if not isinstance(resources, list):
                    resources = []

                if not isinstance(projects, list):
                    projects = []

                if not isinstance(hours, (int, float)):
                    hours = 0

                total_hours += hours

                # ROADMAP CARD
                safe_skill = html.escape(str(skill))
                safe_description = html.escape(str(description))

                st.markdown(
                    f"""
                    <div class="roadmap-card">
                        <div class="skill-title">
                            Step {index + 1}: {safe_skill}
                        </div>
                        <p>{safe_description}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                # EXPANDABLE LEARNING DETAILS
                with st.expander(f"📚 Learn {skill}"):

                    topic_col, resource_col = st.columns(2)

                    with topic_col:
                        st.markdown("### 📖 Topics")

                        if topics:
                            for topic in topics:
                                st.write(f"• {topic}")
                        else:
                            st.write("No topics available yet.")

                    with resource_col:
                        st.markdown("### 🔗 Resources")

                        if resources:
                            for resource in resources:

                                # Expected format: (title, URL)
                                if (
                                    isinstance(resource, (tuple, list))
                                    and len(resource) == 2
                                ):
                                    title, url = resource
                                    st.markdown(
                                        f"[{title}]({url})"
                                    )

                                elif isinstance(resource, str):
                                    st.markdown(
                                        f"[Open resource]({resource})"
                                    )

                                else:
                                    st.write(str(resource))

                        else:
                            st.write("No resources available yet.")

                    st.markdown("### 🛠️ Practice Projects")

                    if projects:
                        for project in projects:
                            st.write(f"• {project}")
                    else:
                        st.write("No projects available yet.")

                    st.info(
                        f"⏱️ Estimated learning time: **{hours} hours**"
                    )

            # FINAL GOAL
            st.markdown(
                f"""
                <div class="goal-card">
                    <h2>🎯 Final Goal</h2>
                    <p>
                        Your learning route starts with
                        <strong>{html.escape(current_skill)}</strong>
                        and ends with
                        <strong>{html.escape(target_skill)}</strong>.
                    </p>
                    <p>
                        Total estimated learning time:
                        <strong>{total_hours} hours</strong>
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown(
    """
    <div class="footer">
        LearnGraph AI • Personalized Learning with Knowledge Graphs
    </div>
    """,
    unsafe_allow_html=True
)