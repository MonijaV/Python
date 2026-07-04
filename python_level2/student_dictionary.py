student={"Name":"Jegan","Age":28,"Grade":"O","Subject":"Maths"}
print(student)
for key,values in student.items():
    print(f"{key} is {values}")
student.update({"Passed":True})
print(student)