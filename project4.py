"""
Python Programming - Project 4: The General Knowledge Quiz
DecodeLabs Industrial Training Kit

Concepts: input(), .strip().lower() sanitization, if-else control flow,
score accumulator (state), and f-string output.
"""

print("=" * 40)
print("   WELCOME TO THE GENERAL KNOWLEDGE QUIZ")
print("=" * 40)
print("Answer 3 questions. +1 point for each correct answer.\n")

# State initialization (integer accumulator)
score = 0

# ---------- Question 1 ----------
answer = input("Q1: What is the capital of France? ")
answer = answer.strip().lower()          # sanitize: remove spaces, normalize case
if answer == "paris":                    # evaluate
    print("Correct! +1 point\n")
    score += 1
else:
    print("Wrong! The correct answer is Paris.\n")

# ---------- Question 2 ----------
answer = input("Q2: Which planet is known as the Red Planet? ")
answer = answer.strip().lower()
if answer == "mars":
    print("Correct! +1 point\n")
    score += 1
else:
    print("Wrong! The correct answer is Mars.\n")

# ---------- Question 3 ----------
answer = input("Q3: How many days are there in a week? ")
answer = answer.strip().lower()
if answer == "7" or answer == "seven":
    print("Correct! +1 point\n")
    score += 1
else:
    print("Wrong! The correct answer is 7.\n")

# ---------- Final result ----------
print("=" * 40)
print(f"Quiz over! Your final score is {score} out of 3.")
if score == 3:
    print("Perfect score! Excellent work!")
elif score == 2:
    print("Great job!")
elif score == 1:
    print("Good try, keep learning!")
else:
    print("Better luck next time!")
print("=" * 40)