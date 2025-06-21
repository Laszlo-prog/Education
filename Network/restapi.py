#C. REST API Automation with requests
import requests

url = "https://api.meraki.com/api/v1/devices"
headers = {"X-Cisco-Meraki-API-Key": "YOUR_API_KEY"}

response = requests.get(url, headers=headers)
print(response.json())  # Get device list in JSON