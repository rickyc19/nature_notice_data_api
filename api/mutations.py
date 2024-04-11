from ariadne import convert_kwargs_to_snake_case
from .db_handler import db_handler
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
        event_host_dict["id"] = db_handler.upsert_event_hosts_table(event_host_dict)
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
        calendar_event_dict["id"] = db_handler.upsert_calendar_events_table(calendar_event_dict)
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