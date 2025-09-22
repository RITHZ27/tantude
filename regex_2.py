import re
s="""Neighbor ID     Pri   State           Dead Time   Address         Interface
100.1.1.1         1   FULL/BDR        00:00:35    2.0.0.1         GigabitEthernet0/0
102.1.1.1         1   FULL/DR         00:00:35    3.0.0.2         GigabitEthernet0/1
107.1.1.1         0   FULL/  -        00:00:35    4.0.0.2         Serial0/0/0"""
pattern=r"(\d+\.\d+\.\d+\.\d+).*?(\d+\.\d+\.\d+\.\d+)\s+(\S+)"
matches=re.findall(pattern, s)
# print(matches)
for match in matches:
    if match[1]=='2.0.0.1':
        print(str(match[1])+"'s neighbors id is "+str(match[0])+" connected via "+str(match[2]))
# op=>2.0.0.1's neighbour id is 100.1.1.1 connected via GigabitEthernet0/0