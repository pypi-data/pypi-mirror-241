from datetime import datetime, timedelta

class TimeDeltaBuilder:
    """Internal class to build timedelta objects based on the called attribute."""
    def __init__(self, value):
        self.value = value

    def minute(self):
        return timedelta(minutes=self.value)

    def minutes(self):
        return self.minute()

    def hour(self):
        return timedelta(hours=self.value)

    def hours(self):
        return self.hour()

    def day(self):
        return timedelta(days=self.value)

    def days(self):
        return self.day()

    def week(self):
        return timedelta(weeks=self.value)

    def weeks(self):
        return self.week()

    def month(self):
        return timedelta(days=self.value * 30)  # approximation

    def months(self):
        return self.month()

    def decade(self):
        return timedelta(days=self.value * 365.25 * 10)  # approximation, considering leap years

    def decades(self):
        return self.decade()

    def leapyear(self):
        return timedelta(days=self.value * 366)  # approximation for leap years

    def leapyears(self):
        return self.leapyear()

class TimeInt:
    def __init__(self, value):
        if not isinstance(value, int):
            raise ValueError("TimeInt requires an integer value. Provided: {}".format(type(value)))
        self.value = value

    @property
    def minute(self):
        return TimeDeltaBuilder(self.value).minute()

    @property
    def hour(self):
        return TimeDeltaBuilder(self.value).hour()

    @property
    def day(self):
        return TimeDeltaBuilder(self.value).day()

    @property
    def week(self):
        return TimeDeltaBuilder(self.value).week()

    @property
    def month(self):
        return TimeDeltaBuilder(self.value).month()

    @property
    def decade(self):
        return TimeDeltaBuilder(self.value).decade()

    @property
    def leapyear(self):
        return TimeDeltaBuilder(self.value).leapyear()

    @staticmethod
    def ago(self):
        return datetime.utcnow() - self.value