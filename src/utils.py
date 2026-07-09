def calculate_average(scores):
    return sum(scores) / len(scores)

def get_result(score):
    if score >= 50:
        return "Pass"
    else:
        return "Fail"
