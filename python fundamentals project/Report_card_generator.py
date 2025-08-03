def calculate_grade(percentage):
    if percentage >= 90:
        return 'A+'
    elif percentage >= 80:
        return 'A'
    elif percentage >= 70:
        return 'B'
    elif percentage >= 60:
        return 'C'
    elif percentage >= 50:
        return 'D'
    else:
        return 'F'

def main():
    student_name = input("Enter student name: ")
    roll_number = input("Enter roll number: ")
    subjects = ["Math", "Science", "English"]
    marks = {}
    total = 0

    for subject in subjects:
        while True:
            try:
                mark = float(input(f"Enter marks for {subject} (out of 100): "))
                if 0 <= mark <= 100:
                    marks[subject] = mark
                    total += mark
                    break
                else:
                    print("Marks should be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")

    percentage = total / len(subjects)
    grade = calculate_grade(percentage)

    # Print Report
    print("\n===== Report Card =====")
    print(f"Name       : {student_name}")
    print(f"Roll No.   : {roll_number}")
    for subject, mark in marks.items():
        print(f"{subject:<10}: {mark}")
    print(f"Total      : {total}")
    print(f"Percentage : {percentage:.2f}%")
    print(f"Grade      : {grade}")

    # Save to File
    filename = f"report_{roll_number}.txt"
    with open(filename, "w") as file:
        file.write("===== Report Card =====\n")
        file.write(f"Name       : {student_name}\n")
        file.write(f"Roll No.   : {roll_number}\n")
        for subject, mark in marks.items():
            file.write(f"{subject:<10}: {mark}\n")
        file.write(f"Total      : {total}\n")
        file.write(f"Percentage : {percentage:.2f}%\n")
        file.write(f"Grade      : {grade}\n")

    print(f"\n✅ Report saved as: {filename}")

if __name__ == "__main__":
    main()


