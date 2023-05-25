# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians
# Assume a year has 365.25 days
from datetime import datetime,timedelta
def get_data():
    with open('10k_racetimes.txt', 'rt') as file:
        content = file.readlines()
    return content

def get_event_time(line):
    """Given a line with Jennifer Rhines' race times from 10k_racetimes.txt, 
       parse it and return a tuple of (age at event, race time).
       Assume a year has 365.25 days"""
    time , _, _, _, rday, rmon, ryear, bday, bmon, byear ,*_= line.split()
    rdate = datetime.strptime(":".join([rday,rmon,ryear]),"%d:%b:%Y")
    bdate = datetime.strptime(":".join([bday, bmon, byear]), "%d:%b:%Y")
    year = (rdate-bdate).days//365.25
    days = int((rdate-bdate).days-year*365.25)
    return  str(int(year))+"y"+str(days)+"d" , time

def get_age_slowest_times():
    '''Return a tuple (age, race_time) where:
       age: AyBd is in this format where A and B are integers'''
    races = get_data()
    rage = 0
    ttime = 0
    rtime = timedelta(0)
    for race in races:
        if "Jennifer Rhines" in race:
            age , event_time = get_event_time(race)
            ttime = event_time
            event_time = list(map(float,event_time.split(":")))
            event_time = timedelta(minutes=event_time[0],seconds=event_time[1])
            if event_time > rtime:
                rtime = event_time
                ntime = ttime
                rage = age
    return rage , ntime
print(get_age_slowest_times())
