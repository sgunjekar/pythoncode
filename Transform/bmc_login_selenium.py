import requests

with open("jwt_token.txt", "r") as f:
    token = f.read()

headers = {
    "Authorization": f"Bearer {token.strip()}",
    "Content-Type": "application/json"
}

response = requests.get("https://aramco-private-dev.qa.sps.secops.bmc.com/", headers=headers)

print("Status Code:", response.status_code)
print("Headers:", response.headers)
print("Raw Response Text:", response.text)
print(response.status_code, response.json())