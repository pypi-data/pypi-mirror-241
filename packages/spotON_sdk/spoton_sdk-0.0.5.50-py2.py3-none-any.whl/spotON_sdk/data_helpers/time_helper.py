from datetime import datetime,timedelta
import pytz 
import pandas as pd


def get_today_midnight(timezone_string: str)->pd.Timestamp:
    CET_TZ = pytz.timezone(timezone_string)

    # get the current date and time in Lisbon timezone
    now_local_tz = pd.Timestamp.now(tz=CET_TZ)

    # set the time to 0:00
    today_midnight = now_local_tz.floor('D')
    return today_midnight

def add_day_to_timestamp(today_timestamp:pd.Timestamp):
    calculate_tomorrow_timestamp = (today_timestamp + pd.DateOffset(days=1)).normalize()
    return calculate_tomorrow_timestamp

def getTime(timezone:str):
    '''Get the current time in UTC timezone'''
    now_utc = datetime.now(pytz.utc)

    # Convert the current time to your desired timezone
    desired_timezone = pytz.timezone(timezone)
    now_local = now_utc.astimezone(desired_timezone)
    return now_local



def tommorow_DayAhead_Prices_ready():

    dateTime = datetime.utcnow()

    if dateTime.hour >= 13:
        print ("There are new entries")
        return True
    else:
        print ("Query all from ")
        return False


def n_days_ago_or_future_midnight(now_local, n,hour = 23):
    # Add or subtract n days from the current date
    n_days_ago_or_future = now_local + timedelta(days=n)

    # Create a new datetime object for n days ago or in the future at 0:00 (midnight)
    n_days_ago_or_future_midnight = datetime(n_days_ago_or_future.year, n_days_ago_or_future.month, n_days_ago_or_future.day, hour, 0)

    return n_days_ago_or_future_midnight

def preview_Timeslot():
    now_local = getTime(timezone='Europe/Berlin')
    if tommorow_DayAhead_Prices_ready(now_local):
        print  ("Query from yesterday day until tomorrow 23:00")
        startTime = n_days_ago_or_future_midnight(now_local,-1,0)
        endTime = n_days_ago_or_future_midnight(now_local,1,23)
    else:
        print  ("Query from two days before until today 23:00")
        startTime = n_days_ago_or_future_midnight(now_local,-2,0)
        endTime = n_days_ago_or_future_midnight(now_local,0,23)

    formatted_startTime = startTime.strftime('%Y-%m-%dT%H:%M:%S%z')
    formatted_endTime = endTime.strftime('%Y-%m-%dT%H:%M:%S%z')

    return formatted_startTime,formatted_endTime

def debug():
    print ("Debug")

    formatted_startTime,formatted_endTime = preview_Timeslot()
    print (f"{formatted_startTime=}\n{formatted_endTime=}")


