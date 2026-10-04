# GraphlearnAI-
My project on the basis of learning from data structure by implementing shortest path and knowledge graph 
LearnGraph AI is a personalized learning roadmap application that uses a Knowledge Graph to help learners move from their current skill to a desired target skill.

The system analyzes skill prerequisites and generates a structured learning path. It also provides learning materials such as topics, resources, projects, and estimated learning hours.

The application is built using Python, NetworkX, and Streamlit.

Features
Personalized learning roadmap generation
Knowledge Graph-based skill relationships
Prerequisite identification
Next-skill identification
Learning path generation
Learning topics for each skill
Curated learning resources
Practical project suggestions
Estimated learning hours
Interactive Streamlit interface

How It Works

The project consists of three main components:

1. Knowledge Graph — data.py

data.py contains the core learning data used by the application.

It includes:

Skills
Skill prerequisites
Learning materials
Topics
Learning resources
Projects
Estimated learning hours

The prerequisite relationships define how one skill leads to another.


2. Graph Processing — graph.py

graph.py uses NetworkX to process the Knowledge Graph.

It is responsible for:

Constructing the directed Knowledge Graph
Representing prerequisite relationships
Finding learning paths
Identifying prerequisites
Identifying direct prerequisites
Identifying next skills

The graph follows the relationship:

Prerequisite → Skill


3. User Interface — app.py

app.py provides the interactive interface using Streamlit.

Learners can:

Select their current skill.
Select their target skill.
Generate a personalized learning roadmap.
View recommended learning steps.
View topics and learning resources.
Complete practical projects.
