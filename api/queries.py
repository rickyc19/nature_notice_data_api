from ariadne import convert_kwargs_to_snake_case
from .db_schemas import CalendarEvent


def list_calendar_events_resolver(obj, info):
    try:
        calendar_events = [calendar_event.to_dict() for calendar_event in CalendarEvent.query.all()]
        print(calendar_events)
        payload = {
            "success": True,
            "calendar_events": calendar_events
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload


@convert_kwargs_to_snake_case
def get_calendar_event_resolver(obj, info, id):
    try:
        calendar_event = CalendarEvent.query.get(id).to_dict()
        print(calendar_event)
        payload = {
            "success": True,
            "calendar_event": calendar_event
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": ["CalendarEvent item matching {id} not found"]
        }
    return payload
