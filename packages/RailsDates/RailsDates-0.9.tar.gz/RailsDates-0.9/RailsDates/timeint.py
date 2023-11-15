from datetime import datetime, timedelta

class TimeDeltaBuilder:
    """Internal class to build timedelta objects based on the called attribute."""
    def __init__(self, value):
        self.value = value
        self.delta = timedelta()

    @property
    def minute(self):
        self.delta += timedelta(minutes=self.value)
        return self

    @property
    def minutes(self):
        return self.minute

    @property
    def hour(self):
        self.delta += timedelta(hours=self.value)
        return self

    @property
    def hours(self):
        return self.hour

    @property
    def day(self):
        self.delta += timedelta(days=self.value)
        return self

    @property
    def days(self):
        return self.day

    @property
    def week(self):
        self.delta += timedelta(weeks=self.value)
        return self

    @property
    def weeks(self):
        return self.week

    @property
    def month(self):
        self.delta += timedelta(days=self.value * 30)  # Approximation
        return self

    @property
    def months(self):
        return self.month

    @property
    def decade(self):
        self.delta += timedelta(days=self.value * 365.25 * 10)  # Approximation, considering leap years
        return self

    @property
    def decades(self):
        return self.decade

    @property
    def leapyear(self):
        self.delta += timedelta(days=self.value * 366)  # Approximation for leap years
        return self

    @property
    def leapyears(self):
        return self.leapyear

    def ago(self):
        return datetime.utcnow() - self.delta

class TimeInt:
    def __init__(self, value):
        if not isinstance(value, int):
            raise ValueError("TimeInt requires an integer value. Provided: {}".format(type(value)))
        self.value = value

    @property
    def minute(self):
        return TimeDeltaBuilder(self.value).minute

    @property
    def minutes(self):
        return self.minute

    @property
    def hour(self):
        return TimeDeltaBuilder(self.value).hour

    @property
    def hours(self):
        return self.hour

    @property
    def day(self):
        return TimeDeltaBuilder(self.value).day

    @property
    def days(self):
        return self.day

    @property
    def week(self):
        return TimeDeltaBuilder(self.value).week

    @property
    def weeks(self):
        return self.week

    @property
    def month(self):
        return TimeDeltaBuilder(self.value).month

    @property
    def months(self):
        return self.month

    @property
    def decade(self):
        return TimeDeltaBuilder(self.value).decade

    @property
    def decades(self):
        return self.decade

    @property
    def leapyear(self):
        return TimeDeltaBuilder(self.value).leapyear

    @property
    def leapyears(self):
        return self.leapyear
