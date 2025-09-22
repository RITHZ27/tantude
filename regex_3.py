import re
s="""
  Internet Address      Physical Address      Type
  10.1.1.1              0030.f29b.0c01        dynamic
  10.1.1.2              000d.bd5d.2eb0        dynamic
  """
pattern=r'(\d+\.\d+\.\d+\.\d+)\s+([0-9a-fA-F\.]+)\s+(\w+)'
out = re.findall(pattern, s)
for ip,mac,dyn in out:
    print(f"IP: {ip}, MAC: {mac}, Type: {dyn}")

