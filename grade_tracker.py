course = input("Enter course name: ")
print("1. Calculate my current final grade")
print("2. Calculate the exam grade I need")

choice = input("Choose 1 or 2: ")
if choice == "1":
  homework = float(input("Enter homework grade: "))
  homework_weight = float(input("Enter homework weight: "))
  quiz = float(input("Enter quiz grade: "))
  quiz_weight = float(input("Enter quiz weigh: "))
  exam = float(input("Enter exam grade: "))
  exam_weight = float(input("Enter exam weight: "))
  if homework_weight + quiz_weight + exam_weight == 100:
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
elif choice == "2":
  homework = float(input("Enter homework grade: "))
  homework_weight = float(input("Enter homework weight: "))
  quiz = float(input("Enter quiz grade: "))
  quiz_weight = float(input("Enter quiz weigh: "))
  exam_weight = float(input("Enter exam weight: "))
  target_grade = float(input("Enter your target grade: "))
  if homework_weight + quiz_weight + exam_weight == 100:
    required_grade = (target_grade - homework * (homework_weight / 100) - quiz * (quiz_weight / 100)) / (exam_weight /100)
    if required_grade > 100:
      print("The maximum exam grade is 100. Try improving your homework or quiz grades")
    elif 0 < required_grade <= 100:
      print(f"you need at least {required_grade:.2f} on the exam to reatch your target grade")
    else:
      print("Congratulations! you already reached your target grade ^_^")
  else:
    print("The total weight must equal 100%")
else:
  print("The content is invalid")
   
  
  
