# Source of data: https://www.arrs.run/
# This dataset has race times for women 10k runners from the Association of Road Racing Statisticians

import re
import datetime


def get_data():
    """Return content from the 10k_racetimes.txt file"""
    with open('10k_racetimes.txt', 'rt') as file:
        content = file.readlines()
    return content


def get_rhines_times():
    """Return a list of Jennifer Rhines' race times"""
    races = get_data()

    times = []
    for race in races:
        time, _, name, *_ = race.split()
        # print(name,time)

        if "rhines" == name.lower().strip("-"):
            times.append(time)
    print(times)
    return times


def get_average():
    """Return Jennifer Rhines' average race time in the format:
       mm:ss:M where :
       m corresponds to a minutes digit
       s corresponds to a seconds digit
       M corresponds to a milliseconds digit (no rounding, just the single digit)"""
    racetimes = get_rhines_times()
    total_time = datetime.timedelta(0)
    for time in racetimes:
        times = list(map(float,time.replace(".",":").split(":")))

        if len(times) == 2:
            minutes , sec = times
            m_m = 0
        else:
            minutes , sec , m_m = times

        dtime = datetime.timedelta(minutes=minutes, seconds=sec,milliseconds=m_m)
        total_time += dtime
        print(total_time)
    return str(total_time/len(racetimes))[2:9]

get_rhines_times()
print(get_average())
