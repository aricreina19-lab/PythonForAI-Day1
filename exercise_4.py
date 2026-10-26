def calculate_total(scores):
    return sum(scores)


def calculate_average(scores):
    if len(scores) == 0:
        return 0
    return sum(scores) / len(scores)


def classify_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def count_passed(scores):
    return sum(1 for score in scores if score >= 60)


# Test calculate_total()
print(calculate_total([80, 90, 70]))  # 240
print(calculate_total([50, 60, 85]))  # 195

# Test calculate_average()
print(calculate_average([80, 90, 70]))  # 80.0
print(calculate_average([50, 60, 90]))  # 66.666...

# Test classify_grade()
print(classify_grade(95))  # A
print(classify_grade(65))  # D

# Test count_passed()
print(count_passed([80, 45, 70, 30, 90]))  # 3
print(count_passed([50, 60, 75, 85]))      # 3