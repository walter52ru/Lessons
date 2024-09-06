students_grade={}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_sorted = (sorted(students))
for i in range(len(students)):
    a = students_sorted[i]
    b = sum(grades[i])/len(grades[i])
    students_grade.update({a:b})
print(students_grade)
