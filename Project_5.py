#FIZZ- BUZZ
# for number in range(0,100):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)


# Average Student Height - using for loop
# student_heights = input("Input a list of student heights. ").split()
# for n in student_heights:
#     student_heights[n] = int(student_heights[n])
# total_height = 0
# for height in student_heights:
#     total_height += height
#
# total_students = 0
# for student in student_heights:
#     total_students += 1
#
# average_height = total_height/total_students
# print(average_height)


# Highest Score

student_scores = input("Input a list of student scores.")
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
highest_score = student_scores[0]
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"Highest score in the class is: {highest_score}" )