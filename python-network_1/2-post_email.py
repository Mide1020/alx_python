import requests
import sys

if len(sys.argv) != 2:
    print("Usage: {} <URL>".format(sys.argv[0]))
    sys.exit(1)

url = sys.argv[1]

response = requests.get(url)
status_code = response.status_code

if status_code >= 400:
    print("Error code:", status_code)
else:
    print(response.text)