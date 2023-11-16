from datetime import datetime

from fameio.source import FameTime
from fameio.source.time import DATE_FORMAT as FAME_DATE_FORMAT

DATE_FORMAT = "%Y-%m-%d_%H:%M:%S"
WIDGET_DATE_FORMAT = "dd/MM/yyyy hh:mm:ss"
WIDGET_DATE_FORMAT_CONSOLE = "%d/%m/%Y %H:%M:%S"


def get_min_fame_date_time_obj() -> object:
    """Get the minimum date time object which represents a 0 in  FAME time"""
    date_time_str = "01/01/2000 00:00:00"
    date_time_obj = datetime.strptime(date_time_str, "%d/%m/%Y %H:%M:%S")
    return date_time_obj


def convert_gui_datetime_to_fame_time(widget_datetime_text: str) -> int:
    """Converts a string into a FAME time integer"""
    widget_datetime_text = widget_datetime_text.replace(".", "/")
    date_time_obj = datetime.strptime(widget_datetime_text, "%d/%m/%Y %H:%M:%S")
    date_string = date_time_obj.strftime(FAME_DATE_FORMAT)
    fame_time: int = FameTime.convert_datetime_to_fame_time_step(date_string)
    return fame_time


def convert_datetime_to_fame(fame_time_string) -> int:
    """Converts a string into a FAME time integer"""
    return FameTime.convert_datetime_to_fame_time_step(
        fame_time_string.strftime(FAME_DATE_FORMAT)
    )


def convert_fame_time_to_gui_datetime(fame_time_string: int) -> object:
    """Converts a FAME time integer into a datetime object"""
    datetime_string = FameTime.convert_fame_time_step_to_datetime(fame_time_string)
    date_time_obj = datetime.strptime(datetime_string, FAME_DATE_FORMAT)
    return date_time_obj
