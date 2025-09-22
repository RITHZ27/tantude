import re
s="""2025-09-10 12:01:45 INFO User login from 192.168.1.10
2025-09-10 12:03:21 ERROR Failed connection attempt from 10.0.0.5
2025-09-10 12:01:45 INFO User login from 192.168.1.10
2025-09-10 12:03:21 ERROR Failed connection attempt from 10.0.0.5
2025-09-10 12:05:12 INFO User logout from 172.16.0.7
2025-09-10 12:07:33 WARN Suspicious traffic from 192.168.1.10"""
l1=[]
count={}
pattern=r"\b(((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9]))\b"
matches=(re.findall(pattern,s))
print(matches)
# for match in matches:
#     l1.append(match[0])
#     if match[0] in count:
#         count[match[0]]+=1
#     else:
#         count[match[0]]=1
# print(count)
# for i in count.values():
#     if i>1:
#         print(count{i})
# # for k,v in count.items():
# #     print(v)
# #     if v>1:
# #         count.pop(v=1)
# #         # print()

    