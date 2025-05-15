import requests

# payload = {'username':'corey' , 'password':'testing'}
# r = requests.post('https://httpbin.org/post',data=payload)
# r_dict = r.json()
# print(r_dict['form'])

def extract_from_json(data, dot_path):
    keys = dot_path.split(".")
    for key in keys:
        if isinstance(data, dict) and key in data:
            data = data[key]
        else:
            return None  # or raise Exception(f"Key {key} not found")
    return data
response = {
    "response": {
        "auth": {
            "token": "abc123"
        }
    }
}

path = "response.auth.token"
print(value)  # Output: abc123
value = extract_from_json(response, path)
