name = input("Enter student's name: ")
age = int(input("Enter student's age: "))
score = float(input("Enter Python score: "))
print(f"Name: {name} (Type: {type(name)})")
print(f"Age: {age} (Type: {type(age)})")
print(f"Score: {score} (Type: {type(score)})")
age_next_year = age + 1
print(f"Age next year: {age_next_year}")