num_students = int(input("Enter number of students: "))
students = []  
for i in range(num_students):
  print(f"\nEnter details for student {i+1}:")
  name = input("Enter student name: ")
  marks=[]
  for j in range(2):
    mark=int(input(f"\nEnter the marks for subject{j+1}: "))
    marks.append(mark)

   # Store in dictionary
  student = {"name": name, "marks": marks}
  students.append(student)

for student in students:
  total_marks = sum(student["marks"])  # sum of marks
  average = total_marks / len(student["marks"])


  if average >= 80:
        grade = "A"
  elif average >= 60:
        grade = "B"
  elif average >= 40:
        grade = "C"
  else:  
     grade = "F"
  student["total"] = total_marks
  student["average"] = average
  student["grade"] = grade

print("\n--- Student Report ---")
for student in students:
    print(f"Name: {student['name']}")
    print(f"Total Marks: {student['total']}")
    print(f"Average: {student['average']:.2f}")
    print(f"Grade: {student['grade']}")
    print("----------------------")
