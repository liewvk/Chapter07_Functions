from student_utils import (
    calculate_average,
    add_results,
    count_results
)


def display_report(students):
    average_score = calculate_average(students)
    excellent_count, pass_count, fail_count = count_results(students)

    print("Student Analysis Report")
    print("-----------------------")

    for student in students:
        print(
            f"Name: {student['name']}, "
            f"Score: {student['score']}, "
            f"Result: {student['result']}"
        )

    print()
    print("Summary")
    print("-------")
    print(f"Number of students: {len(students)}")
    print(f"Average score: {average_score:.2f}")
    print(f"Excellent: {excellent_count}")
    print(f"Pass: {pass_count}")
    print(f"Fail: {fail_count}")


students = [
    {"name": "Alice", "score": 85},
    {"name": "Ben", "score": 72},
    {"name": "Cathy", "score": 90},
    {"name": "David", "score": 45},
    {"name": "Ella", "score": 58}
]

students = add_results(students)
display_report(students)
