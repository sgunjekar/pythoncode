import re

def extract_email_from_file(filepath):
    with open( 'email.txt', 'r') as f:
        #return [line.strip() for line in f if re.search(r"\b[A-Za-z0-9._]+@[A-Za-z0-9-]+\.[A-Z|a-z]+{2,}(?:\.[A-Za-z]{2,})?\b",line)]
         return [ re.findall(r"\b[A-Za-z0-9._]+@[A-Za-z0-9-]+\.[A-Z|a-z]{2,}\b", line) for line in f]
emails = extract_email_from_file('email.txt')
flat_list = [email for sublist in emails for email in sublist]
print(flat_list)
