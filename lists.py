#Lists
#lists are mutable updatable

marks=[50,75,85,"sunil"]

bharat=[1,2,3]

marks=[50,75,85,"sunil",bharat]

print(type(marks))
print(marks)

print(marks [4][1])

marks.extend([95,85])

print(marks)

marks.insert(3, "Varma")

print (marks)

marks[1:1]=["congrats","AEE","saab"]

print(marks)

#deleting items for list

del(marks[1])
print(marks)

del(marks[7][2])

print(marks)

marks.remove("AEE")
print(marks)

print(marks.pop(1))

print(marks)

print(marks.pop())
print(marks)








