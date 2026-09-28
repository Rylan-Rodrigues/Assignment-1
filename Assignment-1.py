#Python Programming Assignment 1
#Operations on List, Tuple and Dictionary

L=[30,10,50,20,40]
print("Original List=", L)
L.append(60)
print(L)
L.insert(2,25)
print(L)
L.remove(25)
print(L)
L.pop()
print(L)
L.sort()
print(L)

t=(10,20,30,20,40)
print("Original Tuple=", t)
print(t.count(20))
print(t.index(30))
print(len(t))
print(max(t))
print(min(t))

students={"name":"Anil","age":18,"branch":"CSE"}
print("Original Dictionary=", students)
students.update({"college":"MITWPU"})
print(students)
print(students.get("name"))
print(students.keys())
print(students.values())
print(students.pop("age"))
