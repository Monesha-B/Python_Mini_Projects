# Input a Python list of student heights
student_heights = input().split()
count = 0
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  count = student_heights[n] + count
  average = count/(len(student_heights))
  average = int(average)
print(f"total height = {count}")
print(f"number of students = {len(student_heights)}")
print(f"average height = {round(average,0)}")


# Input a Python list of student heights
student_heights = input().split()
count = 0
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  count = student_heights[n] + count
  average = count/(len(student_heights))
  average = int(average)
print(f"total height = {count}")
print(f"number of students = {len(student_heights)}")
round_format = "{:.0f}".format(average)
print(f"average height = {round_format}")