from datetime import datetime, timedelta

class TimeDeltaBuilder:
    """Internal class to build timedelta objects based on the called attribute."""
    def __init__(self, value):
        self.value = value
        self.delta = timedelta()

    @property
    def minutes(self):
        self.delta += timedelta(minutes=self.value)
        return self

    @property
    def hours(self):
        self.delta += timedelta(hours=self.value)
        return self

    @property
    def days(self):
        self.delta += timedelta(days=self.value)
        return self

    @property
    def weeks(self):
        self.delta += timedelta(weeks=self.value)
        return self

    @property
    def months(self):
        self.delta += timedelta(days=self.value * 30)  # Approximation
        return self

    @property
    def decades(self):
        self.delta += timedelta(days=self.value * 365.25 * 10)  # Approximation, considering leap years
        return self

    @property
    def leapyears(self):
        # An approximation assuming leap years occur almost every 4 years
        self.delta += timedelta(days=self.value * 366)
        return self

    def ago(self):
        return datetime.utcnow() - self.delta

class TimeInt:
    def __init__(self, value):
        if not isinstance(value, int):
            raise ValueError("TimeInt requires an integer value. Provided: {}".format(type(value)))
        self.value = value

    @property
    def minutes(self):
        return TimeDeltaBuilder(self.value).minutes

    @property
    def hours(self):
        return TimeDeltaBuilder(self.value).hours

    @property
    def days(self):
        return TimeDeltaBuilder(self.value).days

    @property
    def weeks(self):
        return TimeDeltaBuilder(self.value).weeks

    @property
    def months(self):
        return TimeDeltaBuilder(self.value).months

    @property
    def decades(self):
        return TimeDeltaBuilder(self.value).decades

    @property
    def leapyears(self):
        return TimeDeltaBuilder(self.value).leapyears