def create_report_card():
    # Define student data (you can add more students and subjects)
    students = [
        {"name": "Mary", "subject": "Literature", "marks": 172, "grade": "B-"},
        {"name": "Caro", "subject": "Social Science", "marks": 130, "grade": "B-"},
        # Add more student data here
    ]

    # Create a report card string
    report_card = ""
    for student in students:
        report_card += f"Name: {student['name']}\n"
        report_card += f"Subject: {student['subject']}\n"
        report_card += f"Marks: {student['marks']}\n"
        report_card += f"Grade: {student['grade']}\n\n"

    return report_card

def save_report_to_file(report_card, filename="student_report.txt"):
    with open(filename, "w") as file:
        file.write(report_card)

def main():
    report_card_data = create_report_card()
    print(report_card_data)  # Display the report card

    # Save the report card data to a file
    save_report_to_file(report_card_data)

if __name__ == "__main__":
    main()