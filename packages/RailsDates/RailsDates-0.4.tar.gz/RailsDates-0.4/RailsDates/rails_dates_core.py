from datetime import datetime

class RailsDates:
    
    @staticmethod
    def full_day_of_week(date):
        """Returns the full name of the day of the week for the provided date."""
        return date.strftime('%A')

    @staticmethod
    def abbreviated_day(date):
        """Returns the three-letter abbreviation of the day of the week for the provided date."""
        return date.strftime('%a')

    @staticmethod
    def current_month():
        """Returns the full name of the current month."""
        return datetime.utcnow().strftime('%B')

    @staticmethod
    def abbreviated_month(date):
        """Returns the three-letter abbreviation of the month for the provided date."""
        return date.strftime('%b')

    @staticmethod
    def to_s(date, format="%Y-%m-%d %H:%M:%S"):
        """Converts provided date to a readable string in the specified format."""
        return date.strftime(format)

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
