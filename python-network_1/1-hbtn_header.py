import requests
import sys

if len(sys.argv) != 2:
    print("Usage: {} <URL>".format(sys.argv[0]))
    sys.exit(1)

url = sys.argv[1]

response = requests.get(url)
request_id = response.headers.get('X-Request-Id')

print(request_id)