from collections import defaultdict
from pprint import pprint
text = """Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        50G   20G   28G  42% /
tmpfs           1.9G     0  1.9G   0% /dev/shm
tmpfs           1.9G  2.1M  1.9G   1% /run
/dev/sdb1       100G   70G   30G  70% /data
tmpfs           1.9G   48K  1.9G   1% /tmp"""
# """
# 1) split above text into lines
# 2) first line, first word  has to be the key for inner dictionary
# 3) remaining line is comma seperated values dictionary
# dict_df =
# """
lines = text.strip().split('\n')
# print(lines[0])
headers_key = lines[0].split()
# print(headers_key)
dict_df ={}

for line in lines[1:]:
    values = line.split()
    dict_df[values[0]] = list(zip(headers_key, line.split()))

pprint(dict_df)