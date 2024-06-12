grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
u = sorted(students)
a = grades[0]
b = grades[1]
j = grades[2]
k = grades[3]
s = grades[4]
i = {u[0]: sum(a)/len(a), u[1]:sum(b)/len(b), u[2]:sum(j)/len(j), u[3]:sum(k)/len(k), u[4]:sum(s)/len(s)}
print(i)