from ariadne import convert_kwargs_to_snake_case
from .db_schemas import CalendarEvent, EventHost
from .db_helpers import fetch_all_entry, fetch_single_entry


def list_calendar_events_resolver(obj, info):
    return fetch_all_entry(CalendarEvent)


@convert_kwargs_to_snake_case
def get_calendar_event_resolver(obj, info, id):
    return fetch_single_entry(CalendarEvent, id)


def list_event_hosts_resolver(obj, info):
    return fetch_all_entry(EventHost)


@convert_kwargs_to_snake_case
def get_event_host_resolver(obj, info, id):
    return fetch_single_entry(EventHost, id)
