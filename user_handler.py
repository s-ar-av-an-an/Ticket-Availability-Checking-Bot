import csv

# csv file order
# username,movie,date,link,email,freq

def add_entry(entry):
    user = entry[0]
    if not isDuplicate(user):
        with open(f'UserInfo/{user}.csv','w') as f:
            writer = csv.writer(f)
            writer.writerow(entry)

def isDuplicate(uname):
    try:
        with open(f'UserInfo/{uname}.csv','r') as f:
            return True
    except:
        return False

# this function works only for termux version of this app
def remove(user):
    path = os.path.abspath(f"UserInfo/{user}.csv")
    os.system(f"rm {path}")
