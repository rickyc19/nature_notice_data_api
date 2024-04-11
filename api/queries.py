from ariadne import convert_kwargs_to_snake_case
from .db_schemas import CalendarEvent, EventHost


def fetch_all_data(db_object):
    try:
        data = [item.to_dict() for item in db_object.query.all()]
        print(data)
        return {"success": True, db_object.__tablename__: data}
    except Exception as error:
        return {"success": False, "errors": [str(error)]}


def fetch_single_data(db_object, id):
    try:
        data = db_object.query.get(id).to_dict()
        return {"success": True, db_object.__tablename__[:-1]: data}
    except AttributeError:
        return {"success": False, "errors": [f"{db_object.__name__} item matching {id} not found"]}


def list_calendar_events_resolver(obj, info):
    return fetch_all_data(CalendarEvent)


@convert_kwargs_to_snake_case
def get_calendar_event_resolver(obj, info, id):
    return fetch_single_data(CalendarEvent, id)


def list_event_hosts_resolver(obj, info):
    return fetch_all_data(EventHost)


@convert_kwargs_to_snake_case
def get_event_host_resolver(obj, info, id):
    return fetch_single_data(EventHost, id)
