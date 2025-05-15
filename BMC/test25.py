import requests

url = "https://restcountries.com/v3.1/all"
response = requests.get(url)
#json_data= response.json()
# print(json_data)

countries = response.json()
for country in countries:
  languages= country.get('languages')
  if languages:
      # print(languages)
      for language_code , language_name in languages.items():
          # print(f'{language_code}  {language_name}')
           if language_name == 'English':
               country_name = country.get('name', {}).get('common')



               if country_name:
                   print(f'{country_name} ')