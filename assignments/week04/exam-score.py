score = []


score_student1 = int(input("student 1 : "))
score_student2 = int(input("student 2 : "))
score_student3 = int(input("student 3 : "))
score_student4 = int(input("student 4 : "))
score_student5 = int(input("student 5 : "))

score.append(score_student1)
score.append(score_student2)
score.append(score_student3)
score.append(score_student4)
score.append(score_student5)

print(score)

for i in range(5) :
    if score[i] >= 50 :
        print("pass")
    else :
        print("not pass")
    score[i]
