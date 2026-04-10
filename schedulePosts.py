from icalendar import Calendar, Event, Alarm
from datetime import datetime, timedelta
import eel
import pytz

@eel.expose
def createCalendarEvent(title, description, day_of_week, hour, minute, repeat_type):
    cal = Calendar()
    cal.add('prodid', '-//RSMS Scheduler//')
    cal.add('version', '2.0')

    event = Event()
    event.add('summary', title)
    event.add('description', description)

    tz = pytz.timezone("America/Phoenix")

    today = datetime.now(tz)
    target_weekday = get_weekday_index(day_of_week)

    days_ahead = target_weekday - today.weekday()
    if days_ahead <= 0:
        days_ahead += 7

    start_time = today + timedelta(days=days_ahead)
    start_time = start_time.replace(hour=hour, minute=minute, second=0, microsecond=0)

    event.add('dtstart', start_time)
    event.add('dtstamp', datetime.now(tz))

    rrule = {}

    if repeat_type == "none":
        pass
    elif repeat_type == "daily":
        rrule['freq'] = 'DAILY'
    elif repeat_type == "weekly":
        rrule['freq'] = 'WEEKLY'
        rrule['byday'] = day_of_week[:2].upper()
    elif repeat_type == "monthly":
        rrule['freq'] = 'MONTHLY'
        rrule['bymonthday'] = start_time.day
    
    if rrule:
        event.add('rrule', rrule)

    alarm = Alarm()
    alarm.add('action', 'DISPLAY')
    alarm.add('description', 'Reminder to make a post on social media!')
    alarm.add('trigger', timedelta(minutes=-10))

    event.add_component(alarm)
    cal.add_component(event)

    filename = f"scheduled_post_{day_of_week}_{hour}_{minute}.ics"
    with open(filename, 'wb') as f:
        f.write(cal.to_ical())

    print(f"Calendar file created :{filename}")
    return filename

def get_weekday_index(day):
    days = {
        "monday":0,
        "tuesday":1,
        "wednesday":2,
        "thursday":3,
        "friday":4,
        "saturday":5,
        "sunday":6
    }
    return days[day.lower()]