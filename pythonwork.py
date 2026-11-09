import streamlit as st

# Set page layout and title
st.set_page_config(page_title="Python helper", page_icon="🐍", layout="wide")

st.title("🐍 Python Study Companion & Quiz Hub")
st.write("Welcome! This simple tool helps you review concepts and test your knowledge.")

# Sidebar navigation 
st.sidebar.header("Navigation")
choice = st.sidebar.radio(
    "Choose a Module:",
    [
        "Unit I: Introduction to python & Data Types",  
        "Unit II: Control & Logic",
        "Unit III: Functions & Data Structures",
        "Interactive Syllabus Quiz"
    ]
)

st.sidebar.markdown("---")

# ---------------------------------------------------------
# UNIT I: Introduction & Data Types
# Concepts: Intro to Python, Variables, Data Types
# ---------------------------------------------------------
if choice == "Unit I: Introduction & Data Types":
    st.header("Unit I: Introduction & Data Types")
    st.write("Welcome to Python! Learn what Python is and explore how variables and data types work.")

    st.subheader("1. What is Python?")
    st.write(
        "Python is a popular, high-level programming language known for its simplicity and readability. "
        "It uses dynamic typing, meaning that you don't have to declare a variable's type explicitly before using it."
    )
    st.subheader("2. Interactive Data Type Explorer")
    st.write("Enter different values below to see how Python interprets their data types (`str`, `int`, `float`, `bool`).")
    
    col1, col2 = st.columns(2)

    with col1:
        # Taking different types of inputs
        user_str = st.text_input("Enter some text (String):", value="Hello Python!")
        user_int = st.number_input("Enter a whole number (Integer):", value=42, step=1)
        user_float = st.number_input("Enter a decimal (Float):", value=3.14, step=0.1)
        user_bool = st.checkbox("Toggle for Boolean (True/False)", value=True)

    with col2:
        st.write("**Python's Built-in `type()` output:**")
        # Displaying the types dynamically
        st.code(
            f"type({repr(user_str)}) -> {type(user_str).__name__}\n"
            f"type({user_int}) -> {type(user_int).__name__}\n"
            f"type({user_float}) -> {type(user_float).__name__}\n"
            f"type({user_bool}) -> {type(user_bool).__name__}"
        )
        
    st.info("💡 **Notice:** Python automatically assigns the correct data type based on the value you provide!")

# ---------------------------------------------------------
# UNIT II: Control Structures & Exception Handling
# Concepts: Conditionals, Loops, Pattern Programs, Exceptions
# ---------------------------------------------------------
elif choice == "Unit II: Control & Logic":
    st.header("Unit II: Control Structures & Logic")

    st.subheader("1. Grade Evaluator (Conditional Statements)")
    score = st.slider("Select Student Marks (0 to 100):", min_value=0, max_value=100, value=75)

    if score >= 90:
        grade = "A+ (Outstanding)"
    elif score >= 75:
        grade = "A (Very Good)"
    elif score >= 60:
        grade = "B (Good)"
    elif score >= 40:
        grade = "C (Pass)"
    else:
        grade = "F (Fail)"

    st.success(f"Score: **{score}** | Result: **{grade}**")

    st.markdown("---")
    st.subheader("2. Pattern Generator (Loops & Nested Loops)")
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
    st.subheader("3. Safe Division (Exception Handling)")
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
# Concepts: Functions, Strings, Lists, Tuples, Dicts, Sets
# ---------------------------------------------------------
elif choice == "Unit III: Functions & Data Structures":
    st.header("Unit III: Functions & Data Structures")

    # Helper function demonstration
    def analyze_text(text):
        char_count = len(text)
        word_count = len(text.split())
        vowels = "aeiouAEIOU"
        vowel_count = sum(1 for char in text if char in vowels)
        return char_count, word_count, vowel_count

    st.subheader("1. String Analysis (Using Functions)")
    user_string = st.text_area("Enter any text snippet:", "Python programming is fun and structured.")

    if user_string:
        c_count, w_count, v_count = analyze_text(user_string)
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Characters", c_count)
        col2.metric("Total Words", w_count)
        col3.metric("Vowel Count", v_count)

    st.markdown("---")
    st.subheader("2. Data Structure Operations")

    ds_type = st.radio("Select Data Structure:", ["List", "Tuple", "Dictionary", "Set"])

    if ds_type == "List":
        sample_list = ["Python", "Variables", "Loops", "Functions"]
        st.write("**Sample List:**", sample_list)
        new_item = st.text_input("Add new item to list:", "Data Structures")
        if st.button("Append Item"):
            sample_list.append(new_item)
            st.write("**Updated List:**", sample_list)

    elif ds_type == "Tuple":
        sample_tuple = ("Unit I", "Unit II", "Unit III")
        st.write("**Sample Tuple (Immutable):**", sample_tuple)
        st.info(f"First element: `{sample_tuple[0]}` | Length: `{len(sample_tuple)}`")

    elif ds_type == "Dictionary":
        syllabus_dict = {
            "Unit I": "Introduction & Data Types",
            "Unit II": "Control Structures",
            "Unit III": "Functions & Data Structures"
        }
        st.write("**Syllabus Map (Keys & Values):**", syllabus_dict)

    elif ds_type == "Set":
        sample_set = {"Loops", "Functions", "Variables", "Loops"} # Duplicate automatically removed
        st.write("**Sample Set (Unique Elements Only):**", sample_set)

# ---------------------------------------------------------
# INTERACTIVE QUIZ MODULE
# ---------------------------------------------------------
elif choice == "Interactive Syllabus Quiz":
    st.header("📝 Python Syllabus Knowledge Check")

    quiz_score = 0

    q1 = st.radio(
        "1. Which of the following data structures is immutable?",
        ["List", "Dictionary", "Tuple", "Set"],
        index=None
    )
    if q1 == "Tuple":
        quiz_score += 1

    q2 = st.radio(
        "2. Which keyword is used in Python to handle exceptions?",
        ["try / except", "do / catch", "if / else", "error / handle"],
        index=None
    )
    if q2 == "try / except":
        quiz_score += 1

    # Updated Q3 to match the Data Types theme instead of Operators
    q3 = st.radio(
        "3. Which built-in function is used to find the data type of a variable?",
        ["find()", "datatype()", "type()", "check()"],
        index=None
    )
    if q3 == "type()":
        quiz_score += 1

    if st.button("Submit Answers"):
        st.subheader(f"Your Final Score: {quiz_score} / 3")
        if quiz_score == 3:
            st.balloons()
            st.success("Excellent! Perfect score on syllabus fundamentals.")
        else:
            st.info("Good attempt! Review Units I-III and try again.")
