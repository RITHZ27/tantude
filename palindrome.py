s=list(input("enter a list of strings:").split(","))
print(s)
for item in s:
    if item.strip()==item.strip()[::-1]:
        print(str(item)+" is a palindrome")
    else:
        print(str(item)+" is not a palindrome")
        