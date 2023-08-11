import requests

url = "https://intranet.hbtn.io/status"

response = requests.get(url)
response_type = str(type(response.text))
response_content = response.text

print("Body response:")
print("\t- type:", response_type)
print("\t- content:", response_content)