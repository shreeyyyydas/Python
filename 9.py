#create:
student = {
    1:{"name":"Miley","age":21,"city":"L.A."},
    2:{"name":"Cyprus","age":25,"city":"Santiago"},
    3:{"name":"Newton","age":30,"city":"Chile"}
    }

print("After create:", student)

# READ: Accessing values
print("Student Name:", student[1]["name"])
print("Student Age:", student[2]["age"])
print("Student city:", student[3]["city"])

# UPDATE: Modifying existing value
student[3]["age"] = 21
print("After update:", student)

# DELETE: Removing a key-value pair
del student[2]
print("After delete:", student)
