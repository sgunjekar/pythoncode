import requests
import pandas as pd

# Step 2: Fetch data
url = "https://restcountries.com/v3.1/all"
response = requests.get(url)
countries = response.json()

# Step 2: Build a flat list of records: one per country
records = []
for country in countries:
    name = country.get("name", {}).get("common")
    languages = country.get("languages", {})
    if isinstance(languages, dict) and 'English' in languages.values():
        records.append({"Country": name})

# Step 3: Create a DataFrame
df = pd.DataFrame(records)

# Step 4: Print result
print(df)
