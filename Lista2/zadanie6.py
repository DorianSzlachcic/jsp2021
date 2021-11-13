a = ["Kasia","Basia","Marek","Darek"]

a.append("Jozek")

a.extend(["Ania", "Basia"])

a.sort()

print(a[3])
print(a[0:2])
print(a[len(a)-2:len(a)])

a.remove("Basia")
a.remove("Basia")

print("Ilość studentów: " + str(len(a)))

b = tuple(a)