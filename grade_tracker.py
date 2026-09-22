course = input("Enter course name: ")
homework = float(input("Enter homework grade: "))
homework_weight = float(input("Enter homework weight: "))
quiz = float(input("Enter quiz grade: "))
quiz_weight = float(input("Enter quiz weigh: "))
exam = float(input("Enter exam grade: "))
exam_weight = float(input("Enter exam weight: "))
print(course)
print(homework)
print(homework_weight)
print(quiz)
print(quiz_weight)
print(exam)
print(exam_weight)
if homework_weight + quiz_weight + exam_weight == 100:
  final_grade = homework * (homework_weight / 100) + quiz * (quiz_weight / 100) + exam * (exam_weight /100)
  print(final_grade)
  if final_grade >= 90:
    print("A")
  elif final_grade >= 80: # No upper bound is needed because final_grade can be a float, such as 89.5
    print("B")
  elif final_grade >= 70:
    print("C")
  elif final_grade >= 60:
    print("D")
  else:
    print("F")
else:
  print("The total weight must equal 100%")


