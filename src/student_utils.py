def calculate_average(students):
    total_score = 0

    for student in students:
        total_score += student["score"]

    return total_score / len(students)


def classify_score(score):
    if score >= 80:
        return "Excellent"
    elif score >= 50:
        return "Pass"
    else:
        return "Fail"


def add_results(students):
    for student in students:
        student["result"] = classify_score(student["score"])

    return students


def count_results(students):
    excellent_count = 0
    pass_count = 0
    fail_count = 0

    for student in students:
        if student["result"] == "Excellent":
            excellent_count += 1
        elif student["result"] == "Pass":
            pass_count += 1
        else:
            fail_count += 1

    return excellent_count, pass_count, fail_count
