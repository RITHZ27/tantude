l1=input("enter the names:").split(",")
l1.sort()
with open("listfile.txt","w") as f:
    for i in l1:
        f.write(i+"\n")
with open("listfile.txt","r") as f:
    data = f.read().splitlines()
print(str(data[::-1])+"->descending")
print(str(data)+"->ascending")