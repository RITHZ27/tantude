import re
s="""Interface             IP-Address  OK? Method Status Protocol
GigabitEthernet0/0     192.168.1.1     YES manual up   up
GigabitEthernet0/1     unassigned      YES unset administratively down down
FastEthernet0/0        10.0.0.1        YES manual up   up
Loopback0              127.0.0.1       YES manual up     up
Vlan1                  172.16.0.1      YES manual down   down
Serial0/0/0            unassigned      YES unset  down   down"""
pattern=r"(\S+\d+).*?(up|down|administratively down)"
matches=re.findall(pattern,s)
op=[]
# print(matches)
for match in matches:
    op.append({"interface":match[0],"status":match[1]})
print(op)
    
