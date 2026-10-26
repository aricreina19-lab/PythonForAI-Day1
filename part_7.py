# def greet():
#     print("hello from UCS Pyay")
# greet()
# def greet(name):
#     print(f"Hello, {name}!")
# greet("Ma Ma")
# greet("Mg Mg")
def calculate_average(scores):
    if len(scores) == 0:
        return  0
    return sum(scores) / len(scores)
scores = [45,70,80]
result =  calculate_average(scores)
print(result)

def calculate_total(scores):
    return sum(scores)

print(calculate_total([80, 90, 70])) 
print(calculate_total([50, 60, 85]))

def classify_grade(score):
    if score >= 90:
      return "A+"
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B+"
    elif score >= 50:
        return "B"
    elif score >= 40:
        return "C"
    elif score >= 30:
        return "D"
    else:
        return "F"

print(classify_grade(20))
print(classify_grade(65))

def count_passed(scores):
    return sum(1 for score in scores if score >= 40)
print(count_passed([80, 25, 70, 30, 90]))