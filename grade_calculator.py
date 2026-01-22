def calculate_grade(marks):
    # Validate marks
    if marks < 0 or marks > 100:
        return "Invalid marks! Please enter marks between 0 and 100."

    # Grade calculation
    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 50:
        grade = "D"
    else:
        grade = "F"

    # Nested condition for remarks
    if grade == "F":
        remark = "Fail – Better luck next time."
    elif grade in ("A+", "A"):
        remark = "Excellent performance!"
    else:
        remark = "Good effort. Keep improving."

    return f"Grade: {grade} | Remark: {remark}"


# Main program
try:
    marks = float(input("Enter your marks (0–100): "))
    result = calculate_grade(marks)
    print(result)
except ValueError:
    print("Invalid input! Please enter numeric values only.")
