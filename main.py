# Student Performance Analyzer
# Python for AI - Day 1 Final Assignment


# Grade Categories
grade_categories = ("Excellent", "Good", "Pass", "Fail")


# Function 1: Calculate Average
def calculate_average(scores):
    if len(scores) == 0:
        return 0

    total = 0

    for score in scores:
        total += score

    average = total / len(scores)

    return average


# Function 2: Classify Grade
def classify_grade(score):
    if score < 0 or score > 100:
        return "Invalid"
    elif score >= 80:
        return "Excellent"
    elif score >= 60:
        return "Good"
    elif score >= 40:
        return "Pass"
    else:
        return "Fail"


# Function 3: Count Passed Students
def count_passed(students):
    count = 0

    for student in students:
        if student["score"] >= 40:
            count += 1

    return count


# Student Information
students = [
    {
        "name": "Aung Aung",
        "age": 21,
        "study_hours": 4.5,
        "score": 85
    },
    {
        "name": "Su Su",
        "age": 20,
        "study_hours": 3.0,
        "score": 65
    },
    {
        "name": "Mg Mg",
        "age": 22,
        "study_hours": 2.5,
        "score": 35
    },
    {
        "name": "Hla Hla",
        "age": 21,
        "study_hours": 5.0,
        "score": 90
    },
    {
        "name": "Kyaw Kyaw",
        "age": 23,
        "study_hours": 3.5,
        "score": 55
    }
]


# Display Student Performance Report
print("===== STUDENT PERFORMANCE REPORT =====")

scores = []

for student in students:

    name = student["name"]
    age = student["age"]
    study_hours = student["study_hours"]
    score = student["score"]

    # Validate Score
    if score < 0 or score > 100:
        grade = "Invalid"
    else:
        grade = classify_grade(score)

    scores.append(score)

    print()
    print("Name:", name)
    print("Age:", age)
    print("Study Hours:", study_hours)
    print("Score:", score)
    print("Grade:", grade)


# Calculate Summary Statistics
total_students = len(students)
average_score = calculate_average(scores)
highest_score = max(scores)
lowest_score = min(scores)
passed_students = count_passed(students)
failed_students = total_students - passed_students


# Find Top Student
top_student = ""

for student in students:
    if student["score"] == highest_score:
        top_student = student["name"]


# Display Summary
print()
print("===== SUMMARY =====")

print("Total Students:", total_students)
print("Average Score:", average_score)
print("Highest Score:", highest_score)
print("Lowest Score:", lowest_score)
print("Passed Students:", passed_students)
print("Failed Students:", failed_students)
print("Top Student:", top_student)

print("Grade Categories:", grade_categories)