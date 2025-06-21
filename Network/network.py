#D. Network Monitoring with ping3
from ping3 import ping

response = ping('google.com')
if response is not None:
    print(f"Ping successful! Response time: {response} ms")
else:
    print("Host is down!")
    