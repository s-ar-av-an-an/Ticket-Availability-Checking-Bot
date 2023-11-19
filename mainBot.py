import sourcedefender
import webScrapper_TicketNew
import dateday
import mail_handler


frequency = 10

class User:
    def __init__(self, link, date, movie, email, username):
        self.link = link
        self.date = date
        self.movie = movie
        self.email = email
        #self.frequency = frequency
        self.username = username

    def check_presence(self):
        soup = webScrapper_TicketNew.initialize(self.link, self.date)
        if soup:
            dateobj = dateday.convert_to_dateday(self.date)
            calendar = webScrapper_TicketNew.get_calender(soup)
            if dateobj in calendar[1]:
                movies_running = webScrapper_TicketNew.get_movie_list(soup)
                if self.movie in movies_running:
                    show_timings = webScrapper_TicketNew.get_movie_times(soup, self.movie)
                    self.sendMail(show_timings)

    def sendMail(self,show_timings):
        mail_handler.processmail(self.email, self.movie, self.link, self.username)
        return True



