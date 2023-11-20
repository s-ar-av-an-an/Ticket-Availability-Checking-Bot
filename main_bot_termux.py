import webScrapper_TicketNew
import dateday
import csv
import sys
import os
import cron_handler


class User:
    def __init__(self, link, date, movie, username):
        self.link = link
        self.date = date
        self.movie = movie
        self.username = username

    def check_presence(self):
        soup = webScrapper_TicketNew.initialize(self.link, self.date)
        if soup:
            dateobj = dateday.convert_to_dateday(self.date)
            calendar = webScrapper_TicketNew.get_calender(soup)
            if dateobj in calendar[1]:
                movies_running = webScrapper_TicketNew.get_movie_list(soup)
                if self.movie in movies_running:
                    return True


file = sys.argv[1]
with open(file, 'r') as f:
    reader = csv.reader(f)
    row = tuple(reader)[0]


user = User(row[4], row[2], row[1], row[0])
flag = user.check_presence()
if flag:
    os.system("termux-notification --sound -c '{} bookings are open'".format(user.movie))
    cron_handler.remove(user.username)
    user_handler.remove(user.username)






