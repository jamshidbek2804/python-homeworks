universities = [
    ["California Institute of Technology", 2175, 37704],
    ["Harvard", 19627, 39849],
    ["Massachusetts Institute of Technology", 10566, 40732],
    ["Princeton", 7802, 37000],
    ["Rice", 5879, 35551],
    ["Stanford", 19535, 40569],
    ["Yale", 11701, 40500],
]

# students = [uni[1] for uni in universities]
# tuition =  [uni[2] for uni in universities]
# print(students)
# print(tuition)

_, students, tuition = zip(*universities)
students = list(students)
tuition = list(tuition)

total_students = sum(students)
total_tuition = sum(tuition)

import statistics

student_mean = statistics.mean(students)
student_median = statistics.median(students)

tuition_mean = statistics.mean(tuition)
tution_median = statistics.median(tuition)

print(f"Total students: {total_students}")
print(f"Total tuition: $ {total_tuition}")
print(f"Student mean: {student_mean: .2f}")
print(f"Student median: {student_median}")
print(f"Tuition mean: {tuition_mean: .2f}")
print(f"Tuition median: {tution_median}")
