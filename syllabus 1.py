import streamlit as st
import csv
import io
import math
import numpy as np
import pandas as pd

# Set page layout and title
st.set_page_config(page_title="Python Syllabus", page_icon="🐍", layout="wide")

st.title("🐍 Python Study Companion & Quiz Hub")
st.write("Welcome! This tool helps you review concepts and test your knowledge")

# Sidebar navigation 
st.sidebar.header("Navigation")
choice = st.sidebar.radio(
    "Choose a Module:",
    [
        "Unit I: Introduction & Data Types",
        "Unit II: Control & Logic",
        "Unit III: Functions & Data Structures",
        "Unit IV: File Handling and Modules",
        "Unit V: Applications of Python",
        "Interactive Syllabus Quiz"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("Tip: Select a unit above to explore interactive syllabus concepts.")

# ---------------------------------------------------------
# UNIT I: Introduction & Data Types
# ---------------------------------------------------------
if choice == "Unit I: Introduction & Data Types":
    st.header("Unit I: Introduction & Data Types")
    st.write("Welcome to Python! Learn what Python is and explore how variables and data types work.")

    st.subheader("1. What is Python?")
    st.write(
        "Python is a popular, high-level programming language known for its simplicity and readability. "
        "It uses dynamic typing, meaning you don't have to declare a variable's type explicitly before using it."
    )

    st.subheader("2. Interactive Data Type Explorer")
    st.write("Enter different values below to see how Python interprets their data types")
    
    col1, col2 = st.columns(2)

    with col1:
        user_str = st.text_input("Enter some text (String):", value="Hello Python!")
        user_int = st.number_input("Enter a whole number (Integer):", value=42, step=1)
        user_float = st.number_input("Enter a decimal (Float):", value=3.14, step=0.1)
        user_bool = st.checkbox("Toggle for Boolean (True/False)", value=True)

    with col2:
        st.write("**Python's Built-in `type()` output:**")
        st.code(
            f"type({repr(user_str)}) -> {type(user_str).__name__}\n"
            f"type({user_int}) -> {type(user_int).__name__}\n"
            f"type({user_float}) -> {type(user_float).__name__}\n"
            f"type({user_bool}) -> {type(user_bool).__name__}"
        )
        
    st.info("💡 **Notice:** Python automatically assigns the correct data type based on the value you provide!")

# ---------------------------------------------------------
# UNIT II: Control Structures & Exception Handling
# ---------------------------------------------------------
elif choice == "Unit II: Control & Logic":
    st.header("Unit II: Control Structures & Logic")

    st.subheader("1. Pattern Generator (Loops & Nested Loops)")
    rows = st.number_input("Enter Number of Rows for Pattern:", min_value=1, max_value=10, value=5)
    pattern_type = st.selectbox("Select Pattern Style:", ["Star Triangle", "Number Pyramid"])

    pattern_output = ""
    if pattern_type == "Star Triangle":
        for i in range(1, rows + 1):
            pattern_output += "*" * i + "\n"
    elif pattern_type == "Number Pyramid":
        for i in range(1, rows + 1):
            pattern_output += (str(i) + " ") * i + "\n"

    st.code(pattern_output, language="text")

    st.markdown("---")
    st.subheader("2. Safe Division (Exception Handling)")
    val_a = st.text_input("Numerator:", value="10")
    val_b = st.text_input("Denominator:", value="0")

    if st.button("Execute Safe Division"):
        try:
            res = float(val_a) / float(val_b)
            st.success(f"Result: {res}")
        except ZeroDivisionError:
            st.error("Exception Caught: `ZeroDivisionError` — Cannot divide by zero!")
        except ValueError:
            st.error("Exception Caught: `ValueError` — Please enter valid numerical inputs.")

# ---------------------------------------------------------
# UNIT III: Functions & Data Structures
# Concepts: Functions, Scope, Recursion, Strings, Lists, Tuples, Dicts, Sets
# ---------------------------------------------------------
elif choice == "Unit III: Functions & Data Structures":
    st.header("Unit III: Functions and Data Structures")

    # 1. Functions & Strings
    def analyze_text(text):
        char_count = len(text)
        word_count = len(text.split())
        vowels = "aeiouAEIOU"
        vowel_count = sum(1 for char in text if char in vowels)
        return char_count, word_count, vowel_count

    st.subheader("1. Functions & String Analysis")
    user_string = st.text_area("Enter any text snippet:", "Python programming is fun and structured.")

    if user_string:
        c_count, w_count, v_count = analyze_text(user_string)
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Characters", c_count)
        col2.metric("Total Words", w_count)
        col3.metric("Vowel Count", v_count)

    st.markdown("---")

    # 2. Scope of Variables & Recursion
    col_scope, col_rec = st.columns(2)

    with col_scope:
        st.subheader("2. Scope of Variables (Local vs. Global)")
        st.write("A **global** variable exists outside functions, while a **local** variable only exists inside the function where it is created.")
        st.code(
            'x = "Global Variable"\n\n'
            'def scope_demo():\n'
            '    x = "Local Variable"\n'
            '    return x\n\n'
            'print(scope_demo())  # Output: Local Variable\n'
            'print(x)             # Output: Global Variable',
            language="python"
        )

    with col_rec:
        st.subheader("3. Recursion (Introduction)")
        st.write("Recursion occurs when a function calls itself until it reaches a **base case**.")
        fact_num = st.number_input("Calculate Factorial recursively (n!):", min_value=0, max_value=12, value=5)

        def factorial(n):
            if n == 0 or n == 1:
                return 1
            return n * factorial(n - 1)

        st.success(f"`factorial({fact_num})` = **{factorial(fact_num)}**")
        st.caption("Base case: `n <= 1` returns `1`. Recursive step: `n * factorial(n - 1)`.")

    st.markdown("---")

    # 3. Data Structures
    st.subheader("4. Data Structure Operations")
    ds_type = st.radio("Select Data Structure:", ["List", "Tuple", "Dictionary", "Set"], horizontal=True)

    if ds_type == "List":
        sample_list = ["Python", "Variables", "Loops", "Functions"]
        st.write("**Sample List (Mutable & Ordered):**", sample_list)
        new_item = st.text_input("Add new item to list:", "Data Structures")
        if st.button("Append Item"):
            sample_list.append(new_item)
            st.write("**Updated List:**", sample_list)

    elif ds_type == "Tuple":
        sample_tuple = ("Unit I", "Unit II", "Unit III")
        st.write("**Sample Tuple (Immutable & Ordered):**", sample_tuple)
        st.info(f"First element: `{sample_tuple[0]}` | Length: `{len(sample_tuple)}`")

    elif ds_type == "Dictionary":
        syllabus_dict = {
            "Unit I": "Introduction & Data Types",
            "Unit II": "Control Structures",
            "Unit III": "Functions & Data Structures",
            "Unit IV": "File Handling & Modules",
            "Unit V": "Applications of Python"
        }
        st.write("**Syllabus Map (Key-Value Pairs):**", syllabus_dict)

    elif ds_type == "Set":
        sample_set = {"Loops", "Functions", "Variables", "Loops"}
        st.write("**Sample Set (Unordered & Unique Elements Only):**", sample_set)

# ---------------------------------------------------------
# UNIT IV: File Handling and Modules
# Concepts: Text/CSV Files, Modules, Packages, NumPy, Pandas
# ---------------------------------------------------------
elif choice == "Unit IV: File Handling and Modules":
    st.header("Unit IV: File Handling and Modules")

    # 1. Reading/Writing Files & CSV
    st.subheader("1. Reading/Writing Text & CSV Files")
    tab_txt, tab_csv = st.tabs(["📄 Text File Simulator", "📊 CSV File Simulator"])

    with tab_txt:
        note_content = st.text_area("Write content to simulate saving to `notes.txt`:", "Line 1: Python File Handling\nLine 2: Using open() with 'r' and 'w' modes.")
        st.code(
            'with open("notes.txt", "w") as file:\n'
            '    file.write(note_content)\n\n'
            'with open("notes.txt", "r") as file:\n'
            '    print(file.read())',
            language="python"
        )
        st.download_button("Download notes.txt", data=note_content, file_name="notes.txt", mime="text/plain")

    with tab_csv:
        st.write("CSV (Comma-Separated Values) files store tabular data. Python's `csv` module parses rows easily.")
        sample_csv = "Topic,Unit,Difficulty\nData Types,Unit I,Easy\nRecursion,Unit III,Medium\nPandas,Unit IV,Medium"
        csv_input = st.text_area("Edit Raw CSV Data:", sample_csv, height=110)
        reader = list(csv.reader(io.StringIO(csv_input)))
        st.write("**Parsed CSV Rows (List of Lists):**", reader)

    st.markdown("---")

    # 2. Modules & Packages
    st.subheader("2. Modules and Packages")
    col_m1, col_m2 = st.columns(2)
    with col_m1:
        st.info("**Module:** A single `.py` file containing reusable functions and variables (e.g., `import math`).")
        num_sqrt = st.number_input("Test `math.sqrt()` from built-in `math` module:", min_value=0, value=25)
        st.write(f"`math.sqrt({num_sqrt})` = **{math.sqrt(num_sqrt):.2f}**")
    with col_m2:
        st.info("**Package:** A folder containing multiple modules and an `__init__.py` file (e.g., `numpy`, `pandas`).")
        st.code("import numpy as np\nimport pandas as pd", language="python")

    st.markdown("---")

    # 3. Intro to NumPy & Pandas
    st.subheader("3. Introduction to NumPy & Pandas")
    col_np, col_pd = st.columns(2)

    with col_np:
        st.write("**NumPy (Numerical Python):** Fast multi-dimensional arrays & math operations.")
        multiplier = st.slider("Multiply NumPy array `[10, 20, 30, 40]` by:", 1, 10, 2)
        arr = np.array([10, 20, 30, 40])
        st.code(f"arr = np.array([10, 20, 30, 40])\narr * {multiplier}  # Output: {arr * multiplier}")

    with col_pd:
        st.write("**Pandas:** Data manipulation using labeled **DataFrames**.")
        df = pd.DataFrame({
            "Student": ["Aarav", "Diya", "Rohan"],
            "Score": [88, 94, 79],
            "Passed": [True, True, True]
        })
        st.dataframe(df, use_container_width=True, hide_index=True)

# ---------------------------------------------------------
# UNIT V: Applications of Python
# Concepts: Data Processing, Automation, Legal Doc Analysis, Web Scraping, AI, Ethics
# ---------------------------------------------------------
elif choice == "Unit V: Applications of Python":
    st.header("Unit V: Applications of Python")

    # 1. Interactive Legal Document Analysis & Automation Demo
    st.subheader("1. Automated Legal Document Analysis (Demo)")
    st.write("Python automates tedious workflows—such as scanning contracts for key legal clauses and risk terms.")

    default_contract = (
        "This Non-Disclosure Agreement (NDA) is entered into on November 18, 2026. "
        "The Receiving Party agrees to strict confidentiality and shall not disclose proprietary data. "
        "Any breach of this Agreement shall be governed by arbitration and subject to termination and liability."
    )
    legal_text = st.text_area("Paste a sample contract or legal clause:", default_contract, height=110)

    key_terms = ["confidentiality", "liability", "termination", "arbitration", "indemnity", "breach"]
    if st.button("Scan Document for Legal Keywords"):
        lower_text = legal_text.lower()
        found_terms = [term.capitalize() for term in key_terms if term in lower_text]
        word_total = len(legal_text.split())

        c1, c2 = st.columns(2)
        c1.metric("Total Words Processed", word_total)
        c2.metric("Key Legal Clauses Detected", len(found_terms))

        if found_terms:
            st.success(f"**Detected Clauses:** {', '.join(found_terms)}")
        else:
            st.warning("No standard risk/clause keywords detected in the text.")

    st.markdown("---")

    # 2. Core Real-World Domains
    st.subheader("2. Real-World Python Domains & Ethics")
    col_a, col_b = st.columns(2)

    with col_a:
        st.markdown("**📊 Data Processing & Automation**")
        st.write("Cleaning large datasets, renaming batches of files, sending automated emails, and generating PDF/Excel reports using libraries like `pandas`, `os`, and `openpyxl`.")

        st.markdown("**🕷️ Web Scraping Basics**")
        st.write("Extracting structured data from websites using `requests` to fetch HTML pages and `BeautifulSoup` to parse tags like `<h1>`, `<p>`, and `<a>`.")

    with col_b:
        st.markdown("**🤖 Artificial Intelligence Overview**")
        st.write("Python is the primary language for AI, Machine Learning, and NLP using frameworks like `scikit-learn`, `PyTorch`, and `TensorFlow` for prediction and text generation.")

        st.markdown("**⚖️ Ethics in Programming**")
        st.write("Responsible coding requires respecting `robots.txt` and copyright when scraping, protecting user data privacy, avoiding algorithmic bias in AI models, and ensuring transparency.")

# ---------------------------------------------------------
# INTERACTIVE QUIZ MODULE
# ---------------------------------------------------------
elif choice == "Interactive Syllabus Quiz":
    st.header("📝 Python Syllabus Knowledge Check")

    quiz_score = 0

    q1 = st.radio(
        "1. [Unit I] Which built-in function is used to find the data type of a variable?",
        ["find()", "datatype()", "type()", "check()"],
        index=None
    )
    if q1 == "type()":
        quiz_score += 1

    q2 = st.radio(
        "2. [Unit II] Which keyword pair is used in Python to handle exceptions?",
        ["try / except", "do / catch", "if / else", "error / handle"],
        index=None
    )
    if q2 == "try / except":
        quiz_score += 1

    q3 = st.radio(
        "3. [Unit III] What is required to stop a recursive function from calling itself infinitely?",
        ["A global variable", "A base case", "A tuple", "A loop counter"],
        index=None
    )
    if q3 == "A base case":
        quiz_score += 1

    q4 = st.radio(
        "4. [Unit IV] Which Python library is specifically designed for tabular DataFrames?",
        ["math", "csv", "Pandas", "BeautifulSoup"],
        index=None
    )
    if q4 == "Pandas":
        quiz_score += 1

    q5 = st.radio(
        "5. [Unit V] Which ethical practice should be followed during web scraping?",
        ["Bypassing login walls", "Checking and respecting a site's robots.txt file", "Scraping private user passwords", "Overloading the server with rapid requests"],
        index=None
    )
    if q5 == "Checking and respecting a site's robots.txt file":
        quiz_score += 1

    if st.button("Submit Answers"):
        st.subheader(f"Your Final Score: {quiz_score} / 5")
        if quiz_score == 5:
            st.balloons()
            st.success("Excellent! Perfect score across all 5 syllabus units.")
        else:
            st.info("Good attempt! Review Units I–V and try again.")