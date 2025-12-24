def calculate_grade(marks):
    if marks >= 90:
        return "A", "Excellent work! Outstanding performance!"
    elif marks >= 80:
        return "B", "Very Good! Keep it up!"
    elif marks >= 70:
        return "C", "Good effort. Keep practicing!"
    elif marks >= 60:
        return "D", "You passed, but there is room for improvement."
    else:
        return "F", "Don't give up. Learn from mistakes and try again!"


name = input("Enter student name: ").strip().upper()

while True:
    try:
        marks = int(input("Enter marks (0-100): "))
        if 0 <= marks <= 100:
            break
        else:
            print("Invalid marks. Please enter marks between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter numeric marks only.")


grade, message = calculate_grade(marks)

print("\n📊 RESULT FOR {}:".format(name))
print(f"Marks: {marks}/100")
print(f"Grade: {grade}")
print(f"Message: {message}")
