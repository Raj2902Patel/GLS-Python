questions = []
score = 0

def attempt_quiz():
    global score
    print("Welcome to the Quiz!")
    print("Answer the following questions:")
    print("--------------------------------")
    for question in questions:
        print(question['question'])
        print("Options:")
        for i, option in enumerate(question['options'], start=1):
            print(f"{i}. {option}")
        answer = input("Your answer (enter the option number): ")
        if answer == question['answer']:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
            break
        print("--------------------------------")
    print("Quiz complete!")
    print(f"Your score: {score}/{len(questions)}")
    print()

def add_question():
    question_text = input("Enter the question: ")
    options = []
    for i in range(4):
        option = input(f"Enter option {i+1}: ")
        options.append(option)
    answer = input("Enter the correct option number: ")
    question = {
        'question': question_text,
        'options': options,
        'answer': answer
    }
    questions.append(question)
    print("Question added successfully!")
    print()

while True:
    print("Menu:")
    print("1. Attempt Quiz")
    print("2. Add Question")
    print("3. Quit")
    choice = input("Enter your choice (1-3): ")
    print()

    if choice == '1':
        score = 0
        attempt_quiz()
    elif choice == '2':
        add_question()
    elif choice == '3':
        print("Thank you for using the Quiz program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
        print()
