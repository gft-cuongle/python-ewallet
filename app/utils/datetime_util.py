from datetime import datetime


def diff_time_in_minutes(time_start, time_end):
    ts = datetime.fromtimestamp(time_start / 1000.0)
    te = datetime.fromtimestamp(time_end / 1000.0)
    return int((te - ts).total_seconds() / 60)
