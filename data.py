
# ==================================================
# LearnGraph AI - DATA
# ==================================================

SKILLS = [
    "Programming",
    "Python",
    "Data Structures",
    "Algorithms",
    "Object-Oriented Programming",
    "Databases",
    "SQL",
    "Web Development",
    "HTML & CSS",
    "JavaScript",
    "Git & GitHub",
    "Software Engineering",
    "Data Science",
    "Machine Learning",
    "Artificial Intelligence",
    "Deep Learning",
    "Computer Networks",
    "Operating Systems",
    "Cybersecurity",
    "Cloud Computing"
]


# Each item must contain exactly two skill names:
# (prerequisite, skill)

PREREQUISITES = [
    ("Programming", "Python"),
    ("Programming", "Data Structures"),
    ("Data Structures", "Algorithms"),
    ("Python", "Algorithms"),
    ("Python", "Object-Oriented Programming"),
    ("Programming", "Databases"),
    ("Databases", "SQL"),
    ("Programming", "Web Development"),
    ("Web Development", "HTML & CSS"),
    ("HTML & CSS", "JavaScript"),
    ("Programming", "Git & GitHub"),
    ("Programming", "Software Engineering"),
    ("Python", "Data Science"),
    ("Data Science", "Machine Learning"),
    ("Python", "Machine Learning"),
    ("Machine Learning", "Artificial Intelligence"),
    ("Machine Learning", "Deep Learning"),
    ("Programming", "Computer Networks"),
    ("Programming", "Operating Systems"),
    ("Computer Networks", "Cybersecurity"),
    ("Operating Systems", "Cybersecurity"),
    ("Programming", "Cloud Computing")
]


# Every skill has the same dictionary structure.
# This prevents: 'list' object has no attribute 'get'

LEARNING_MATERIALS = {
    "Programming": {
        "description": "Learn programming fundamentals and computational thinking.",
        "topics": [
            "Programming fundamentals",
            "Variables and data types",
            "Conditions and loops",
            "Functions",
            "Problem-solving"
        ],
        "resources": [
            ("freeCodeCamp", "https://www.freecodecamp.org/learn/"),
            ("W3Schools", "https://www.w3schools.com/")
        ],
        "projects": [
            "Simple calculator",
            "Number guessing game",
            "Quiz application"
        ],
        "hours": 20
    },

    "Python": {
        "description": "Learn Python syntax and build practical programs.",
        "topics": [
            "Python syntax",
            "Variables and data types",
            "Conditions and loops",
            "Functions",
            "Lists and dictionaries",
            "File handling",
            "Exception handling"
        ],
        "resources": [
            ("Official Python Tutorial", "https://docs.python.org/3/tutorial/"),
            ("W3Schools Python", "https://www.w3schools.com/python/")
        ],
        "projects": [
            "Expense tracker",
            "To-do list",
            "Student grade calculator"
        ],
        "hours": 30
    },

    "Data Structures": {
        "description": "Learn how data is organized and accessed efficiently.",
        "topics": [
            "Arrays and lists",
            "Linked lists",
            "Stacks and queues",
            "Hash tables",
            "Trees",
            "Graphs"
        ],
        "resources": [
            ("GeeksforGeeks", "https://www.geeksforgeeks.org/data-structures/"),
            ("VisuAlgo", "https://visualgo.net/")
        ],
        "projects": [
            "Stack implementation",
            "Contact management system",
            "Graph traversal visualizer"
        ],
        "hours": 35
    },

    "Algorithms": {
        "description": "Develop efficient methods for solving computational problems.",
        "topics": [
            "Searching",
            "Sorting",
            "Recursion",
            "Time complexity",
            "Greedy algorithms",
            "Dynamic programming"
        ],
        "resources": [
            ("VisuAlgo", "https://visualgo.net/"),
            ("GeeksforGeeks", "https://www.geeksforgeeks.org/fundamentals-of-algorithms/")
        ],
        "projects": [
            "Sorting visualizer",
            "Shortest-path finder",
            "Algorithm comparison tool"
        ],
        "hours": 40
    },

    "Object-Oriented Programming": {
        "description": "Organize code using classes, objects, and reusable components.",
        "topics": [
            "Classes and objects",
            "Encapsulation",
            "Inheritance",
            "Polymorphism",
            "Abstraction"
        ],
        "resources": [
            ("Python Classes Tutorial", "https://docs.python.org/3/tutorial/classes.html")
        ],
        "projects": [
            "Library management system",
            "Bank account simulator",
            "Inventory application"
        ],
        "hours": 25
    },

    "Databases": {
        "description": "Understand how applications store and manage information.",
        "topics": [
            "Relational databases",
            "Tables and relationships",
            "Keys",
            "Database design",
            "Normalization",
            "Transactions"
        ],
        "resources": [
            ("PostgreSQL Documentation", "https://www.postgresql.org/docs/"),
            ("W3Schools SQL", "https://www.w3schools.com/sql/")
        ],
        "projects": [
            "Student database",
            "Library database",
            "Inventory database"
        ],
        "hours": 25
    },

    "SQL": {
        "description": "Query, filter, and manipulate data in relational databases.",
        "topics": [
            "SELECT queries",
            "Filtering and sorting",
            "Joins",
            "Aggregate functions",
            "Subqueries",
            "INSERT, UPDATE and DELETE"
        ],
        "resources": [
            ("SQLBolt", "https://sqlbolt.com/"),
            ("W3Schools SQL", "https://www.w3schools.com/sql/")
        ],
        "projects": [
            "Sales analysis",
            "Student result reports",
            "Store inventory queries"
        ],
        "hours": 20
    },

    "Web Development": {
        "description": "Understand how websites and web applications are built.",
        "topics": [
            "Frontend and backend",
            "Client-server architecture",
            "HTTP and HTTPS",
            "Web APIs",
            "Authentication",
            "Deployment"
        ],
        "resources": [
            ("MDN Web Development", "https://developer.mozilla.org/en-US/docs/Learn")
        ],
        "projects": [
            "Portfolio website",
            "Blog website",
            "Task management application"
        ],
        "hours": 35
    },

    "HTML & CSS": {
        "description": "Create and style responsive web pages.",
        "topics": [
            "HTML elements",
            "Semantic HTML",
            "Forms",
            "CSS selectors",
            "Flexbox and Grid",
            "Responsive design"
        ],
        "resources": [
            ("MDN HTML", "https://developer.mozilla.org/en-US/docs/Web/HTML"),
            ("MDN CSS", "https://developer.mozilla.org/en-US/docs/Web/CSS")
        ],
        "projects": [
            "Portfolio page",
            "Landing page",
            "Responsive product page"
        ],
        "hours": 20
    },

    "JavaScript": {
        "description": "Add interactive behavior to websites.",
        "topics": [
            "Variables and functions",
            "Arrays and objects",
            "DOM manipulation",
            "Events",
            "Promises",
            "Working with APIs"
        ],
        "resources": [
            ("MDN JavaScript Guide", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide")
        ],
        "projects": [
            "Interactive quiz",
            "Weather application",
            "Expense tracker"
        ],
        "hours": 30
    },

    "Git & GitHub": {
        "description": "Track code changes and collaborate on software projects.",
        "topics": [
            "Repositories",
            "Commits",
            "Branches",
            "Merging",
            "Pull requests",
            "Collaboration"
        ],
        "resources": [
            ("Git Documentation", "https://git-scm.com/doc"),
            ("GitHub Documentation", "https://docs.github.com/")
        ],
        "projects": [
            "Version-control a Python project",
            "Create a project portfolio",
            "Collaborate on a repository"
        ],
        "hours": 12
    },

    "Software Engineering": {
        "description": "Apply structured methods to build maintainable software.",
        "topics": [
            "Requirements analysis",
            "Software design",
            "Modular architecture",
            "Testing",
            "Debugging",
            "Maintenance"
        ],
        "resources": [
            ("pytest Documentation", "https://docs.pytest.org/")
        ],
        "projects": [
            "Tested task manager",
            "Modular student application",
            "Documented software project"
        ],
        "hours": 30
    },

    "Data Science": {
        "description": "Analyze datasets and extract meaningful insights.",
        "topics": [
            "Python for data analysis",
            "NumPy",
            "Pandas",
            "Data cleaning",
            "Statistics",
            "Data visualization"
        ],
        "resources": [
            ("Pandas Documentation", "https://pandas.pydata.org/docs/"),
            ("NumPy Documentation", "https://numpy.org/doc/"),
            ("Matplotlib", "https://matplotlib.org/stable/")
        ],
        "projects": [
            "Sales data analysis",
            "Student performance analysis",
            "Data visualization dashboard"
        ],
        "hours": 40
    },

    "Machine Learning": {
        "description": "Build models that learn patterns from data.",
        "topics": [
            "Supervised learning",
            "Unsupervised learning",
            "Regression",
            "Classification",
            "Model evaluation",
            "Feature engineering"
        ],
        "resources": [
            ("Scikit-learn", "https://scikit-learn.org/stable/user_guide.html"),
            ("Google ML Crash Course", "https://developers.google.com/machine-learning/crash-course")
        ],
        "projects": [
            "House price predictor",
            "Spam classifier",
            "Student performance predictor"
        ],
        "hours": 50
    },

    "Artificial Intelligence": {
        "description": "Explore intelligent systems, search, reasoning, and AI applications.",
        "topics": [
            "AI fundamentals",
            "Search algorithms",
            "Knowledge representation",
            "Reasoning",
            "Machine learning applications",
            "Responsible AI"
        ],
        "resources": [
            ("Google AI Education", "https://ai.google/education/")
        ],
        "projects": [
            "Rule-based expert system",
            "AI study assistant",
            "Knowledge-based recommendation system"
        ],
        "hours": 40
    },

    "Deep Learning": {
        "description": "Study neural networks and models for complex data.",
        "topics": [
            "Neural network fundamentals",
            "Activation functions",
            "Backpropagation",
            "Convolutional neural networks",
            "Model training"
        ],
        "resources": [
            ("TensorFlow Tutorials", "https://www.tensorflow.org/tutorials"),
            ("PyTorch Tutorials", "https://pytorch.org/tutorials/")
        ],
        "projects": [
            "Image classifier",
            "Handwritten digit recognizer",
            "Text classification model"
        ],
        "hours": 50
    },

    "Computer Networks": {
        "description": "Learn how computers communicate and exchange information.",
        "topics": [
            "Network fundamentals",
            "OSI and TCP/IP models",
            "IP addressing",
            "Routing",
            "DNS",
            "TCP and UDP"
        ],
        "resources": [
            ("Cloudflare Learning Center", "https://www.cloudflare.com/learning/")
        ],
        "projects": [
            "Network topology diagram",
            "Client-server application",
            "Network protocol study"
        ],
        "hours": 30
    },

    "Operating Systems": {
        "description": "Understand how operating systems manage computer resources.",
        "topics": [
            "Processes and threads",
            "CPU scheduling",
            "Memory management",
            "Virtual memory",
            "File systems",
            "Synchronization"
        ],
        "resources": [
            ("Operating Systems: Three Easy Pieces", "https://pages.cs.wisc.edu/~remzi/OSTEP/")
        ],
        "projects": [
            "CPU scheduling simulator",
            "Memory allocation simulator",
            "Process monitoring tool"
        ],
        "hours": 35
    },

    "Cybersecurity": {
        "description": "Learn how to protect systems, applications, and information.",
        "topics": [
            "Security fundamentals",
            "Authentication",
            "Cryptography basics",
            "Common vulnerabilities",
            "Network security",
            "Secure coding"
        ],
        "resources": [
            ("OWASP Top 10", "https://owasp.org/www-project-top-ten/"),
            ("CISA Resources", "https://www.cisa.gov/resources-tools")
        ],
        "projects": [
            "Password strength checker",
            "Security checklist",
            "Local security log analyzer"
        ],
        "hours": 35
    },

    "Cloud Computing": {
        "description": "Learn cloud infrastructure and application deployment.",
        "topics": [
            "Cloud service models",
            "Virtual machines",
            "Containers",
            "Cloud storage",
            "Networking",
            "Deployment and monitoring"
        ],
        "resources": [
            ("AWS Training", "https://aws.amazon.com/training/"),
            ("Microsoft Learn", "https://learn.microsoft.com/en-us/training/azure/")
        ],
        "projects": [
            "Deploy a web application",
            "Host a static website",
            "Containerize a Python application"
        ],
        "hours": 35
    }
}