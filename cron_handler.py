import os

def add_cron(row):
    loc = os.path.abspath("main_bot_termux.py")
    csvFile = os.path.abspath(f'UserInfo/{row[0]}.csv')
    cronFile = os.path.abspath(f'cronInfo.txt')
    pypath = os.path.abspath(f'pypath.txt')

    # get python path
    os.system(f"which python > {pypath}")
    with open('pypath.txt','r') as f:
        path = f.read().strip()

    # make a copy of cron jobs
    os.system(f"crontab -l > {cronFile}")
    cmd = f'*/{row[3]} * * * * {path} {loc} {csvFile}'
    with open('cronInfo.txt', 'a') as f:
        f.write(cmd+'\n')

    # add entry to cron tab
    os.system("echo "" | crontab -")
    os.system(f"cat {cronFile} | crontab -")

def remove(user):
    cronFile = os.path.abspath(f'cronInfo.txt')
    # make a copy and remove
    os.system(f"crontab -l > {cronFile}")
    newstr = ''
    with open('cronInfo.txt','r') as f:
        for i in f.readlines():
            if not i.find(f'{user}.csv'):
                newstr += i+'\n'
    with open('cronInfo.txt','w') as f:
        f.write(newstr)

    # rentry into cron tab
    os.system("echo ""|crontab -")
    os.system(f"cat {cronFile} | crontab -")
