import random

questions = {
    'DSA': [
        ("What is the time complexity of binary search?", ["O(log n)", "O(n)", "O(n log n)"], "O(log n)"),
        ("What data structure is used in a Breadth First Search?", ["Stack", "Queue", "Graph"], "Queue"),
        ("Which algorithm is used to find the shortest path in a graph?", ["Bellman-Ford", "Dijkstra", "Prim's"], "Dijkstra"),
        ("What is the primary characteristic of a stack?", ["FIFO", "LIFO", "LILO"], "LIFO"),
        ("In which data structure are elements sorted?", ["Heap", "Array", "Queue"], "Heap"),
        ("What is a self-balancing binary search tree?", ["AVL Tree", "Red-Black Tree", "B-Tree"], "AVL Tree"),
        ("Which sorting algorithm has the best average case time complexity?", ["Bubble Sort", "Merge Sort", "Selection Sort"], "Merge Sort"),
        ("What is the purpose of a hash function?", ["Searching", "Indexing", "Sorting"], "Indexing"),
        ("What is the time complexity of Quick Sort?", ["O(n log n)", "O(n^2)", "O(log n)"], "O(n log n)"),
        ("Which data structure is used for depth-first search?", ["Graph", "Queue", "Stack"], "Stack")
    ],
    'DBMS': [
        ("What does SQL stand for?", ["Structured Query Language", "Simple Query Language", "Structured Query List"], "Structured Query Language"),
        ("What is a primary key?", ["Unique identifier for a record", "A query", "A data type"], "Unique identifier for a record"),
        ("What is a foreign key?", ["A type of key", "Reference to a primary key in another table", "A non-primary key"], "Reference to a primary key in another table"),
        ("Which SQL statement is used to extract data from a database?", ["GET", "SELECT", "RETRIEVE"], "SELECT"),
        ("What is a transaction?", ["A sequence of operations executed as a single unit", "A type of query", "A database"], "A sequence of operations executed as a single unit"),
        ("What is normalization?", ["Process of organizing data to reduce redundancy", "Process of deleting data", "Process of updating data"], "Process of organizing data to reduce redundancy"),
        ("What is an index?", ["A list of columns", "Database object to improve query performance", "A type of query"], "Database object to improve query performance"),
        ("What is ACID property?", ["Atomicity, Consistency, Isolation, Durability", "Authorization, Consistency, Isolation, Durability", "Atomicity, Concurrency, Isolation, Durability"], "Atomicity, Consistency, Isolation, Durability"),
        ("What is a join?", ["Combining rows from two or more tables", "A SQL command", "A database transaction"], "Combining rows from two or more tables"),
        ("What is a stored procedure?", ["A precompiled collection of SQL statements", "A SQL query", "A type of data"], "Precompiled collection of SQL statements")
    ],
    'Python': [
        ("What is a list comprehension?", ["A way to create lists", "A way to declare variables", "A way to handle exceptions"], "Concise way to create lists"),
        ("How do you declare a variable in Python?", ["By assignment", "Using var keyword", "Using let keyword"], "By assignment"),
        ("What is the purpose of the 'def' keyword in Python?", ["Define a function", "Declare a variable", "Create a class"], "Define a function"),
        ("What is a lambda function?", ["A named function", "An anonymous function", "A recursive function"], "Anonymous function"),
        ("What is PEP 8?", ["Python's style guide", "Python's built-in library", "Python's framework"], "Python's style guide"),
        ("What is a decorator?", ["Function that modifies another function", "A Python module", "A type of variable"], "Function that modifies another function"),
        ("How do you handle exceptions in Python?", ["Using try and except blocks", "Using error blocks", "Using catch blocks"], "Using try and except blocks"),
        ("What is the difference between '== 'and 'is'?", ["'==' checks value equality, 'is' checks identity", "'==' checks identity, 'is' checks value equality", "Both check value equality"], "'==' checks value equality, 'is' checks identity"),
        ("What are Python's built-in data types?", ["List, Tuple, Dictionary, Set", "List, Array, Dictionary, Set", "Array, Tuple, Dictionary, Set"], "List, Tuple, Dictionary, Set"),
        ("How do you iterate over a dictionary?", ["Using a for loop with keys() method", "Using a for loop with items() method", "Using a for loop with values() method"], "Using a for loop with items() method")
    ]
}

users = {}
results = {}

def register():
    roll_number = input("Enter Roll Number: ")
    if roll_number in users:
        print("Roll number already registered!")
        return
    name = input("Enter Name: ")
    password = input("Enter Password: ")
    section = input("Enter Section: ")
    users[roll_number] = {'name': name, 'password': password, 'section': section}
    print("Registration successful!")

def login():
    roll_number = input("Enter Roll Number: ")
    password = input("Enter Password: ")
    if roll_number in users and users[roll_number]['password'] == password:
        print("Login successful!")
        return roll_number
    else:
        print("Invalid roll number or password!")
        return None

def attempt_quiz(roll_number):
    print("Choose a subject: 1. DSA 2. DBMS 3. Python")
    subject_choice = input()
    subjects = {1: 'DSA', 2: 'DBMS', 3: 'Python'}
    subject = subjects[int(subject_choice)]

    questions_to_ask = random.sample(questions[subject], 5)
    score = 0
    for q, options, a in questions_to_ask:
        print(q)
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        answer = input("Your answer: ")
        if options[int(answer) - 1] == a:
            score += 1

    print(f"You scored {score} out of 5 in {subject}.")
    if roll_number not in results:
        results[roll_number] = {}
    results[roll_number][subject] = score

def show_results(roll_number):
    if roll_number in results:
        for subject, score in results[roll_number].items():
            print(f"{subject}: {score}/5")
    else:
        print("No results found.")

def main():
    while True:
        print("1. Register\n2. Login\n3. Attempt Quiz\n4. Show Results\n5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            register()
        elif choice == '2':
            roll_number = login()
        elif choice == '3':
            roll_number = login()
            if roll_number:
                attempt_quiz(roll_number)
        elif choice == '4':
            roll_number = login()
            if roll_number:
                show_results(roll_number)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
