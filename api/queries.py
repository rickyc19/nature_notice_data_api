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
