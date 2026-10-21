def calculate_final_grade(homework, homework_weight,
                          quiz, quiz_weight,
                          exam, exam_weight):

    homework_part = homework * (homework_weight / 100)
    quiz_part = quiz * (quiz_weight / 100)
    exam_part = exam * (exam_weight / 100)

    final_grade = homework_part + quiz_part + exam_part

    return final_grade
                            
def calculate_required_exam(homework, homework_weight,
                            quiz, quiz_weight,
                            exam_weight, target_grade):

    homework_part = homework * (homework_weight / 100)
    quiz_part = quiz * (quiz_weight / 100)

    remaining_grade = target_grade - homework_part - quiz_part

    required_exam = remaining_grade / (exam_weight / 100)

    return required_exam
course = input("Enter course name: ")
print("1. Calculate my current final grade")
print("2. Calculate the exam grade I need")

choice = input("Choose 1 or 2: ")
if choice == "1":
    homework = float(input("Enter homework grade: "))
    homework_weight = float(input("Enter homework weight: "))
    quiz = float(input("Enter quiz grade: "))
    quiz_weight = float(input("Enter quiz weight: "))
    exam = float(input("Enter exam grade: "))
    exam_weight = float(input("Enter exam weight: "))

    if homework_weight + quiz_weight + exam_weight == 100:
        final_grade = calculate_final_grade(homework, homework_weight, quiz, quiz_weight, exam, exam_weight)
        print(final_grade)
        if final_grade >= 90:
            print("A")
        elif final_grade >= 80:
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
    quiz_weight = float(input("Enter quiz weight: "))
    exam_weight = float(input("Enter exam weight: "))
    target_grade = float(input("Enter your target grade: "))

    if exam_weight == 0:
        print("Exam weight must be greater than 0")

    elif homework_weight + quiz_weight + exam_weight == 100:
        required_grade = calculate_required_exam(
            homework, homework_weight,
            quiz, quiz_weight,
            exam_weight, target_grade
        )

        if required_grade > 100:
            print("The maximum exam grade is 100. Try improving your homework or quiz grades")
        elif 0 <= required_grade <= 100:
            print(f"You need at least {required_grade:.2f} on the exam to reach your target grade")
        else:
            print("Congratulations! You already reached your target grade ^_^")

    else:
        print("The total weight must equal 100%")

else:
    print("The content is invalid")

   
  
  
