import requests
from functools import reduce


# Dot-notation JSON extractor
def extract_from_json(data, dot_path):
    try:
        return reduce(lambda d, key: d[int(key)] if isinstance(d, list) else d.get(key), dot_path.split("."), data)
    except (TypeError, KeyError, IndexError, ValueError):
        return None


# Call httpbin and parse the JSON
def test_httpbin_json_extraction():
    url = "https://httpbin.org/get"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to fetch from {url}")
        return

    json_data = response.json()
    print("Full JSON response:")
    print(f'{'\n'}{json_data}')m

    # Example dot-paths
    paths = [
        "url",
        "headers.Host",
        "headers.User-Agent",
        "origin"
    ]

    print("\nExtracted fields:")
    for path in paths:
        value = extract_from_json(json_data, path)
        print(f"{path}: {value}")


# Run the test

def test_github_user_info(username="sgunjekar"):
    url = f"https://api.github.com/users/{username}"
    res = requests.get(url)
    json_data = res.json()
    print(f'{'\n'}{json_data}')
    paths = ["login", "name", "public_repos", "created_at"]
    for path in paths:
        print(f"{path}: {extract_from_json(json_data, path)}")

test_httpbin_json_extraction()
test_github_user_info()