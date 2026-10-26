# for i in range(5):
#     print(i)

# scores =[75,35,55,77,60]
# for score in scores:
#     print(score)

# count = 1
# while count <=5:
#     print(count)
#     count +=2

scores = [45, 70, 85, 30, 90, 55]
total = 0
passing = 0
failing = 0
for score in scores:
    total += score

    if score >= 40:
        passing += 1
    else:
        failing += 1

average = total / len(scores)

print("Total score:", total)
print("Average score:", average)
print("Number of pass scores:", passing)
print("Number of fail scores:", failing)

# scores = [45, 70, 85, 30, 90, 55]
# no_fail =0
# no_pass = 0
# for score in scores:
#     if score <=40:
#         no_fail += 1
#     else no_pass += 1