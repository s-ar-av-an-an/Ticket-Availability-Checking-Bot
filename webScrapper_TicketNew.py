from bs4 import BeautifulSoup
import requests

# variables
master_date_class = 'DatesMobile_datesMonthWrap__PqVRz'
master_movie_class = 'CinemaDetailsV2_runningMovieList__yp0bq CinemaDetailsV2_cinMwebSpacing__TEEia'
sub_movie_class = 'MovieSessionsListing_movieDetailsDivHeading__5ARu1'
month_ = 'DatesMobile_monthLabel__8mx9U'
movie_date = 'DatesMobile_movieDateText__w8FxI'
sessions = 'MovieSessionsListing_col2__4GGXs'
green_col = 'greenCol MovieSessionsListing_time__lMGDL'
yellow_col = 'yellowCol MovieSessionsListing_time__lMGDL'
master_session_class = 'MovieSessionsListing_col2__4GGXs'
sub_session_class = 'MovieSessionsListing_timeblock__S_Z44'

def initialize(link, date):
    # get HTML content of the webpage
    html_text = requests.get(link+'?fromdate={}'.format(date)).text
    # create soup object
    soup = BeautifulSoup(html_text, 'html.parser')
    if 'Sorry' in soup.text:
        return None
    return soup

# get calender
def get_calender(soup):
    calender = soup.find('div', class_=master_date_class)
    mon_onsite = calender.find('div', class_=month_)
    avail_dates = []

    # get all dates
    for dates in calender.find_all('a'):
        avail_dates.append(dates.text)
    return mon_onsite, avail_dates


# get movie list
def get_movie_list(soup):
    web_obj = soup.find('div', class_=master_movie_class)
    movie_list = []
    for blocks in web_obj.find_all('div', class_=sub_movie_class):
        for movies in blocks:
            movie_list.append(movies.text)
    return movie_list

# get all show timings
def get_movie_times(soup, mname):
    movies = get_movie_list(soup)
    pos = movies.index(mname)
    session_master = soup.find_all('div', class_=master_session_class)[pos]
    available = [x.text.split('M')[0]+'M' for x in session_master.find_all('div', class_=green_col)]
    fast_filling = [x.text.split('M')[0]+'M' for x in session_master.find_all('div', class_=yellow_col)]
    return available, fast_filling




