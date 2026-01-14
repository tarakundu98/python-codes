n = int(input("Enter number of students: "))
marks = []
total_marks = 0.0
for i in range(n):
    m = float(input(f"Enter marks(0-100) for student {i+1}: "))
    marks.append(m)
    total_marks += m
print("\nMarks of all students:", marks)
print("Total Marks of all students:", total_marks)
print("Average Marks:", total_marks / n)
print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))


pass_count = len([m for m in marks if m >= 40])


print("Number of students who passed (>=40 marks):", pass_count)
print("Number of students who failed (<40 marks):", n - pass_count)

rev_marks = marks[::-1]
print("Marks in reverse order of entry:", rev_marks)

even_marks = [m for m in marks if m % 2 == 0]
print("Even Marks:", even_marks)
