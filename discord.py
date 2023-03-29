import math

ClassSize = int(input("Enter the number of students: "))
SubjectNo = int(input("Enter the number of subjects: "))

StudentName = []
StudentMark = []
DistinctionCount = 0
MeritCount = 0
PassCount = 0
FailCount = 0

for i in range(ClassSize):
    name = input("Enter name of student #" + str(i+1) + ": ")
    StudentName.append(name)
    mark = []
    total_mark = 0
    for j in range(SubjectNo):
        grade = int(input("Enter grade for subject #" + str(j+1) + ": "))
        mark.append(grade)
        total_mark += grade
    StudentMark.append(mark)

    average_mark = round(total_mark / SubjectNo)

    if average_mark >= 70:
        grade = "distinction"
        DistinctionCount += 1
    elif average_mark >= 55:
        grade = "merit"
        MeritCount += 1
    elif average_mark >= 40:
        grade = "pass"
        PassCount += 1
    else:
        grade = "fail"
        FailCount += 1

    print("\nName: " + name)
    print("Combined Total Mark: " + str(total_mark))
    print("Average Mark: " + str(average_mark))
    print("Grade: " + grade)

print("\nClass Statistics:")
print("Distinctions: " + str(DistinctionCount))
print("Merits: " + str(MeritCount))
print("Passes: " + str(PassCount))
print("Fails: " + str(FailCount))
