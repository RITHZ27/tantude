
import random
lst=[]
num=int(input("enter a number:"))
for i in range(100):
    lst.append(random.randint(1,100))
print("A random list is: ",lst)
lst1=lst[num-1::num]
print("The List with a given number interval: ",lst1)
# Bubble Sort
for i in range(len(lst1)):
    for j in range(len(lst1)-i-1):
        if lst1[j]>lst1[j+1]:
            lst1[j],lst1[j+1]=lst1[j+1],lst1[j]
print("sorted list: ",lst1)

