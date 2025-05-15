test_str= '''ERROR: Disk full
INFO: System started
WARNING: CPU usage high
ERROR: Timeout'''

#Write a script to count how many times each log level (INFO, WARNING, ERROR) appears.

 #with open("logfile.txt") as f:
test_str_list = test_str.split()
print(test_str_list)
count = { k: test_str_list.count(k) for k in test_str_list if k=='ERROR:'or k== 'INFO:' or k=='WARNING:' }
print(count)



count1= {k: test_str_list.count(k) for k in test_str_list if k=='ERROR:' or k=='INFO:'}