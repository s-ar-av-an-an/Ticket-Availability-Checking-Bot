import datetime

def convert_to_dateday(date_string):
    x = list(map(int, date_string.split('-')))
    dateobj = datetime.date(x[0], x[1], x[2])
    return dateobj.strftime('%a')+dateobj.strftime('%d')