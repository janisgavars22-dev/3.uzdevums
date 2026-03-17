
# 3.1. Python datu kolekciju prakse

# 1. Izveido sarakstu ar 5+ studentiem (vārds un atzīme)
students = [
    ("Anna", 85),
    ("Jānis", 72),
    ("Līga", 96),
    ("Mārtiņš", 64),
    ("Zane", 91)
]

# 2. Saskaiti saraksta garumu
count_students = len(students)
print("Studentu skaits:", count_students)

# 3. Izvadi pirmo un pēdējo elementu
print("Pirmais students:", students[0])
print("Pēdējais students:", students[-1])

# 4. Pievieno vienu jaunu studentu
students.append(("Edgars", 78))
print("Pievienots: Edgars – 78")

# 5. Atrodi studentu ar augstāko atzīmi
best = max(students, key=lambda x: x[1])
print("Labākais students:", best)

# 6. Atrodi studentu ar zemāko atzīmi
worst = min(students, key=lambda x: x[1])
print("Vājākais students:", worst)

# 7. Filtrē studentus ar atzīmi >= 80
good_students = list(filter(lambda x: x[1] >= 80, students))
print("Studenti ar atzīmi ≥80:", good_students)

# 8. Izmanto enumerate() lai izvadītu formatēti
for i, (name, grade) in enumerate(students, start=1):
    print(f"{i}. {name} — {grade}")


students = [
    ("Anna", 85),
    ("Jānis", 72),
    ("Līga", 96),
    ("Mārtiņš", 64),
    ("Zane", 91)
]

def student_count():
    return len(students)

def first_student():
    return students[0]

def last_student():
    return students[-1]

def add_student(name, grade):
    students.append((name, grade))
    return students

def best_student():
    return max(students, key=lambda x: x[1])

def worst_student():
    return min(students, key=lambda x: x[1])

def good_students():
    return list(filter(lambda x: x[1] >= 80, students))

def enumerate_students():
    return [f"{i}. {name} — {grade}" 
            for i, (name, grade) in enumerate(students, start=1)]
