import re
s="""
1    0001.9722.000d    DYNAMIC      Fa0/2
1    000d.bd5d.2eb0    DYNAMIC      Fa0/1
1    0030.f29b.0c01    DYNAMIC      Fa0/3"""
pattern=r'((\d)\s+([0-9a-fA-F\.]+)\s+(\S+)\s+(\S+))'
output=re.findall(pattern,s)
# print(output)
for vlanId,mac,type,inteface in output:
    print(f"VlanID: {vlanId}, MAC: {mac}, Type: {type}, Interface: {inteface}")