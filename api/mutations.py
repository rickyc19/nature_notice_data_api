from ariadne import convert_kwargs_to_snake_case
from .db_helpers import upsert_into_table, delete_entry
from .db_schemas import CalendarEvent, EventHost
from typing import Optional


@convert_kwargs_to_snake_case
def upsert_event_host_resolver(
        obj,
        info,
        host_calendar_id: str,
        host_name: str,
        host_description: Optional[str] = None,
        host_website: Optional[str] = None,
        host_email: Optional[str] = None):
    try:
        event_host_dict = {
            "host_calendar_id": host_calendar_id,
            "host_name": host_name,
            "host_description": host_description,
            "host_website": host_website,
            "host_email": host_email
        }
        event_host_dict["id"] = upsert_into_table(
            EventHost,
            event_host_dict,
            [EventHost.host_calendar_id]
        )
        payload = {
            "success": True,
            "event_host": event_host_dict
        }
    except Exception as error:  # date format errors
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload


@convert_kwargs_to_snake_case
def upsert_calendar_event_resolver(
        obj,
        info,
        host_event_id,
        host_id,
        event_name, 
        event_description,
        event_price,
        event_start_date,
        event_end_date,
        event_location):
    try:
        calendar_event_dict = {
            "host_event_id": host_event_id,
            "host_id": host_id,
            "event_name": event_name,
            "event_description": event_description,
            "event_price": event_price,
            "event_start_date": event_start_date,
            "event_end_date": event_end_date,
            "event_location": event_location
        }
        calendar_event_dict["id"] = upsert_into_table(
            CalendarEvent,
            calendar_event_dict,
            [CalendarEvent.host_id, CalendarEvent.host_event_id]
        )
        payload = {
            "success": True,
            "calendar_event": calendar_event_dict
        }
    except Exception as error:  # date format errors
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload


@convert_kwargs_to_snake_case
def delete_event_host_resolver(obj, info, id):
    return delete_entry(EventHost, id)


@convert_kwargs_to_snake_case
def delete_calendar_event_resolver(obj, info, id):
    return delete_entry(CalendarEvent, id)
