import calendar
from datetime import datetime, timedelta, timezone
import time

class Time:
    @staticmethod
    def current():
        """Returns the current UTC datetime."""
        return datetime.utcnow()

    @staticmethod
    def current_month():
        """Returns the full name of the current month."""
        return datetime.utcnow().strftime('%B')

    @staticmethod
    def yesterday():
        """Returns the datetime for the start of yesterday."""
        return (datetime.utcnow() - timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)

    @staticmethod
    def tomorrow():
        """Returns the datetime for the start of tomorrow."""
        return (datetime.utcnow() + timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)

    @staticmethod
    def beginning_of_day():
        """Returns the datetime for the start of the current day."""
        return datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)

    @staticmethod
    def end_of_day():
        """Returns the datetime for the end of the current day."""
        return datetime.utcnow().replace(hour=23, minute=59, second=59, microsecond=999999)

    @staticmethod
    def beginning_of_week():
        """Returns the datetime for the start of the current week (Monday)."""
        now = datetime.utcnow()
        return (now - timedelta(days=now.weekday())).replace(hour=0, minute=0, second=0, microsecond=0)

    @staticmethod
    def end_of_week():
        """Returns the datetime for the end of the current week (Sunday)."""
        now = datetime.utcnow()
        return (now + timedelta(days=6 - now.weekday())).replace(hour=23, minute=59, second=59, microsecond=999999)

    @staticmethod
    def full_day_of_week(date):
        """Returns the full name of the day of the week for the provided date."""
        return date.strftime('%A')

    @staticmethod
    def abbreviated_day(date):
        """Returns the three-letter abbreviation of the day of the week for the provided date."""
        return date.strftime('%a')

    @staticmethod
    def abbreviated_month(date):
        """Returns the three-letter abbreviation of the month for the provided date."""
        return date.strftime('%b')

    @staticmethod
    def distance_of_time_in_words(from_time, to_time=None):
        """
        Returns a human-friendly approximation of the time difference. 
        For instance, it would return "about 2 hours" for a time difference of 2 hours and 10 minutes.
        """
        if to_time is None:
            to_time = datetime.utcnow()
        delta = int((to_time - from_time).total_seconds())
        if delta < 60:
            return "less than a minute"
        elif delta < 3600:
            minutes = delta // 60
            return f"about {minutes} minutes"
        elif delta < 86400:
            hours = delta // 3600
            return f"about {hours} hours"
        else:
            days = delta // 86400
            return f"about {days} days"

    @staticmethod
    def beginning_of_month(date):
        """
        Returns the date for the beginning of the month for a given date.
        """
        return date.replace(day=1)

    @staticmethod
    def end_of_month(date):
        """
        Returns the date for the end of the month for a given date.
        """
        next_month = date.replace(day=28) + timedelta(days=4)  # this will never fail
        return next_month - timedelta(days=next_month.day)    

    @staticmethod
    def today():
        """Returns the current date."""
        return datetime.utcnow().date()

    @staticmethod
    def days_in_month(year=None, month=None):
        """Returns the number of days in a given month and year."""
        if year is None:
            year = datetime.utcnow().year
        if month is None:
            month = datetime.utcnow().month
        return calendar.monthrange(year, month)[1]

    @staticmethod
    def days_in_year(year=None):
        """Returns the number of days in a given year."""
        if year is None:
            year = datetime.utcnow().year
        return 366 if calendar.isleap(year) else 365

    @staticmethod
    def find_zone(zone_name):
        """Finds the timezone by its name."""
        try:
            return timezone(zone_name)
        except:
            return None

    @staticmethod
    def rfc3339():
        """Returns the current UTC time in RFC 3339 format."""
        return datetime.utcnow().isoformat() + 'Z'

    @staticmethod
    def zone():
        """Returns the current time zone name."""
        return time.tzname[0]

    @staticmethod
    def to_s(date, format="%Y-%m-%d %H:%M:%S"):
        """Converts provided date to a readable string in the specified format."""
        return date.strftime(format)

    @staticmethod
    def to_i(date_time):
        """Converts a datetime object to an integer timestamp."""
        return int(date_time.timestamp())

    @staticmethod
    def to_a(date_time):
        """Converts a datetime object to an array of elements."""
        return [date_time.year, date_time.month, date_time.day, date_time.hour, date_time.minute, date_time.second, date_time.weekday()]

    @staticmethod
    def to_fs(date_time, format='%Y-%m-%d %H:%M:%S'):
        """Formats a datetime object as a string."""
        return date_time.strftime(format)
