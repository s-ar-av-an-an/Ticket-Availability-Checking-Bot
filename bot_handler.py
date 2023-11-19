import csv
import mainBot
import sys

file = f'UserInfo/{sys.argv[1]}'
with open(file, 'r') as f:
    reader = csv.reader(f)
    row = tuple(reader)[0]
print(row)


user = mainBot.User(row[3],row[2],row[1],row[4],row[0])
user.check_presence()