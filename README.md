# 🧠 General Knowledge Quiz — Project 4

A simple **General Knowledge Quiz** built using Python as part of the **DecodeLabs Industrial Training**.

The program asks the user 3 general knowledge questions, checks the answers, keeps track of the score, and displays the final result.

## 📌 Project Overview

This project demonstrates fundamental Python programming concepts such as:

* User input using `input()`
* String sanitization using `.strip().lower()`
* `if-else` conditional statements
* Score accumulation
* Comparison operators
* Boolean operators
* `f-string` formatting
* Basic program state management

## ✨ Features

* 🧠 3 General Knowledge questions
* ✅ Automatic answer checking
* 🔢 Score tracking
* 🎯 1 point for every correct answer
* 🔤 Accepts answers regardless of uppercase/lowercase
* 🧹 Removes unnecessary spaces from user input
* 🏆 Displays different messages based on the final score

## ❓ Questions Included

The quiz asks:

1. What is the capital of France?
2. Which planet is known as the Red Planet?
3. How many days are there in a week?

### Scoring

| Score | Result                         |
| ----- | ------------------------------ |
| 3/3   | Perfect score! Excellent work! |
| 2/3   | Great job!                     |
| 1/3   | Good try, keep learning!       |
| 0/3   | Better luck next time!         |

## 🛠️ Technologies Used

* **Python 3**
* Standard Python functions and control flow
* No external libraries required

## 📂 Project Structure

```text
Decodelabs-project4/
│
├── project4.py
└── README.md
```

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/abhikhandelwal1243-hue/Decodelabs-project4.git
```

### 2. Open the project folder

```bash
cd Decodelabs-project4
```

### 3. Run the program

```bash
python3 project4.py
```

## 💻 Example Output

```text
========================================
   WELCOME TO THE GENERAL KNOWLEDGE QUIZ
========================================
Answer 3 questions. +1 point for each correct answer.

Q1: What is the capital of France? Paris
Correct! +1 point

Q2: Which planet is known as the Red Planet? Mars
Correct! +1 point

Q3: How many days are there in a week? 7
Correct! +1 point

========================================
Quiz over! Your final score is 3 out of 3.
Perfect score! Excellent work!
========================================
```

## 🔍 Input Validation

The program uses:

```python
answer.strip().lower()
```

This makes the quiz more user-friendly.

For example:

```text
Paris
PARIS
 paris
 PaRiS
```

All are treated as the same answer.

For the third question, the program accepts both:

```text
7
```

and:

```text
seven
```

## 📚 Learning Objectives

This project helped me practice:

* Python variables
* `input()` function
* String methods
* Conditional statements
* `if`, `elif`, and `else`
* Boolean operators
* Incrementing variables
* Score accumulation
* Formatted output
* Basic problem-solving

## 🔮 Future Improvements

Possible improvements include:

* Add more questions
* Add multiple-choice questions
* Randomize questions
* Add different difficulty levels
* Add a timer
* Store high scores
* Create a graphical user interface
* Load questions from a file or database

## 👨‍💻 Author

**Abhishek Sharma**

### DecodeLabs Industrial Training — Project 4

A beginner-friendly Python General Knowledge Quiz created to practice fundamental programming concepts.
