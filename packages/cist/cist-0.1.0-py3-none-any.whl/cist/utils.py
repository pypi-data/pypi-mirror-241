import time


def to_timestamp(dtime):
    "Converts datetime to utc timestamp"
    return int(time.mktime(dtime.timetuple()))

help_text = f'Помощь по модулю cist:\n' \
