from datetime import datetime, timedelta

class TimeDeltaBuilder:
    """Internal class to build timedelta objects based on the called attribute."""
    def __init__(self, value):
        self.value = value

    def minutes(self):
        return timedelta(minutes=self.value)

    def hours(self):
        return timedelta(hours=self.value)

    def days(self):
        return timedelta(days=self.value)

    def weeks(self):
        return timedelta(weeks=self.value)

    def months(self):
        return timedelta(days=self.value * 30)  # approximation

    def decades(self):
        return timedelta(days=self.value * 365.25 * 10)  # approximation, considering leap years

    def leapyears(self):
        # An approximation assuming leap years occur almost every 4 years
        return timedelta(days=self.value * 366)

class TimeInt:
    def __init__(self, value):
        if not isinstance(value, int):
            raise ValueError("TimeInt requires an integer value. Provided: {}".format(type(value)))
        self.value = value

    def minutes(self):
        return TimeDeltaBuilder(self.value)

    def hours(self):
        return TimeDeltaBuilder(self.value)

    def days(self):
        return TimeDeltaBuilder(self.value)

    def weeks(self):
        return TimeDeltaBuilder(self.value)

    def months(self):
        return TimeDeltaBuilder(self.value)

    def decades(self):
        return TimeDeltaBuilder(self.value)

    def leapyears(self):
        return TimeDeltaBuilder(self.value)

    def ago(self, delta_builder):
        return datetime.utcnow() - delta_builder.minutes()
