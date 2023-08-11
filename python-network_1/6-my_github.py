import requests
import sys

if len(sys.argv) != 3:
    print("Usage: {} <mide1020> <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>".format(sys.argv[0]))
    sys.exit(1)

username = sys.argv[1]
access_token = sys.argv[2]

url = "https://api.github.com/user"

response = requests.get(url, auth=(username, access_token))

try:
    json_response = response.json()
    print(json_response.get("id"))
except ValueError:
    print("None")