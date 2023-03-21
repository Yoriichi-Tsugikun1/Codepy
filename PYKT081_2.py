import re

def is_valid_ip(ip):
    pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
    if re.search(pattern, ip):
        for i in ip.split('.'):
            if int(i) > 255:
                return False
        return True
    return False

t = int(input())
for i in range(t):
    ip = input().strip()
    if is_valid_ip(ip):
        print("YES")
    else:
        print("NO")