quiz = {
    "What is the capital of India?": ["New Delhi", "Egypt", "Prayagraj"],
    "Who developed Python?": ["Guido van Rossum", "James Gosling", "Dennis Ritchie"]
}

answers = {
    "What is the capital of India?": "New Delhi",
    "Who developed Python?": "Guido van Rossum"
}

score = 0

for question in quiz:
    print("\n" + question)

    for option in quiz[question]:
        print("-", option)

    user_answer = input("Enter your answer: ")

    if user_answer == answers[question]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
        print("Correct answer is:", answers[question])

print("\nQuiz Finished")
print("Total Score:", score)

if score == len(quiz):
    print("Excellent")
elif score == len(quiz) - 1:
    print("Good")
else:
    print("Average")