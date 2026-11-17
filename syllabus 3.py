import streamlit as st
import numpy as np

# Set page layout and title
st.set_page_config(page_title="Python Helper", page_icon="🐍", layout="wide")

st.title("🐍 Python Study Companion & Quiz Hub")
st.write("Welcome! This tool helps you review concepts and test your knowledge")

# Sidebar navigation 
st.sidebar.header("Navigation")
choice = st.sidebar.radio(
    "Choose a Module:",
    [
        "Unit I: Introduction & Data Types",
        "Unit II: Control & Logic",
        "Unit III: Functions, Scope & Recursion",
        "Unit IV: Introduction to NumPy",
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

    st.subheader("1. Pattern Generator")
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
    st.subheader("2. Safe Division")
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
# UNIT III: Functions, Scope & Recursion
# ---------------------------------------------------------
elif choice == "Unit III: Functions, Scope & Recursion":
    st.header("Unit III: Functions, Scope & Recursion")

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

    col_scope, col_rec = st.columns(2)

    with col_scope:
        st.subheader("2. Scope of Variables")
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
        st.subheader("3. Recursion")
        st.write("Recursion occurs when a function calls itself until it reaches a **base case**.")
        fact_num = st.number_input("Calculate Factorial recursively (n!):", min_value=0, max_value=12, value=5)

        def factorial(n):
            if n == 0 or n == 1:
                return 1
            return n * factorial(n - 1)

        st.success(f"`factorial({fact_num})` = **{factorial(fact_num)}**")
        st.caption("Base case: `n <= 1` returns `1`. Recursive step: `n * factorial(n - 1)`.")

# ---------------------------------------------------------
# UNIT IV: Introduction to NumPy
# ---------------------------------------------------------
elif choice == "Unit IV: Introduction to NumPy":
    st.header("Unit IV: Introduction to NumPy")

    st.subheader("NumPy")
    st.write("Fast multi-dimensional arrays & vectorized math operations.")
    multiplier = st.slider("Multiply NumPy array `[10, 20, 30, 40]` by:", 1, 10, 2)
    arr = np.array([10, 20, 30, 40])
    st.code(f"arr = np.array([10, 20, 30, 40])\narr * {multiplier}  # Output: {arr * multiplier}")

# ---------------------------------------------------------
# INTERACTIVE QUIZ MODULE
# ---------------------------------------------------------
elif choice == "Interactive Syllabus Quiz":
    st.header("📝 Python Knowledge Check")

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
        ["A global variable", "A base case", "A string", "A loop counter"],
        index=None
    )
    if q3 == "A base case":
        quiz_score += 1

    q4 = st.radio(
        "4. [Unit IV] Which Python library is designed for fast numerical arrays and vectorized math?",
        ["NumPy", "math", "random", "csv"],
        index=None
    )
    if q4 == "NumPy":
        quiz_score += 1

    if st.button("Submit Answers"):
        st.subheader(f"Your Final Score: {quiz_score} / 4")
        if quiz_score == 4:
            st.balloons()
            st.success("Excellent! Perfect score across all 4 syllabus units.")
        else:
            st.info("Good attempt! Review Units I–IV and try again.")