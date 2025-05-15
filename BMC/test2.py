
words = ['Success', 'fail', 'Fail', 'success', 'FAIL', 'fail']
match_word= []
unmatched_word= []


filtered = [word for word in words if word == word.lower()]
#print(filtered)

final_list = [ word.capitalize() for word in filtered]
#print(final_list)


with open ("jwt_token.txt") as f:
    errors = [line for line in f if 'ERROR' in line]
    print(errors)

records = ["John,john@example.com", "Sara,sara@test.com"]
emails = [line.split(',')[1] for line in records ]
print(emails)
raw = ['  apple ', ' ', 'banana', '', '  mango']
cleaned = [ line.strip() for line in raw if line.strip()]
print(cleaned)
rows = [
    "apple,banana,mango",
    "grape,kiwi",
    "orange"
]

flat_rows = [ item for item in rows for item in rows.split(',')]
