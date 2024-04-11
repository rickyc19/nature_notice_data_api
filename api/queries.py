from ariadne import convert_kwargs_to_snake_case
from .db_schemas import CalendarEvent, EventHost
from .db_handler import db_handler


def list_calendar_events_resolver(obj, info):
    return db_handler.fetch_all_data(CalendarEvent)


@convert_kwargs_to_snake_case
def get_calendar_event_resolver(obj, info, id):
    return db_handler.fetch_single_data(CalendarEvent, id)


def list_event_hosts_resolver(obj, info):
    return db_handler.fetch_all_data(EventHost)


@convert_kwargs_to_snake_case
def get_event_host_resolver(obj, info, id):
    return db_handler.fetch_single_data(EventHost, id)
