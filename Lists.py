#Student Grades with Lists
studentNames = ['Rana', 'Ahmet', 'Sude', 'Merve']
studentGrades = [
    [85, 98, 65],
    [26, 78, 100],
    [39, 87, 96],
    [95, 94, 86]
]

for i in range(len(studentNames)):
   name = studentNames[i]
   grades = studentGrades[i]
   average = sum(grades) / len(grades)

   print(f"{name}'s average is: {average:.2f}")
