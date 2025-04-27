import time

print("Saad is Here")

username = "Saad"
print(username)


# isko terminal pr chalyenge tou hamre file read hojayegi
# f = open("app.py")
# f.readline()

# isse bh hamre phile read ki ja skte ha
# f = open("app.py")
# f.__next__() 

# terminal se ham apni file read ker sektein hain loop ka zerya aese

for i in open('app.py'):
    print(i)