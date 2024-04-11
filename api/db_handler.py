from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Dict
from api.db_schemas import EventHost, CalendarEvent
from sqlalchemy.dialects.postgresql import insert
from api import url


class DBHandler:
    def __init__(self):
        engine = create_engine(url)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def upsert_into_table(self, table, data_dict, index_elements) -> int:
        insert_statement = insert(table).values(data_dict)

        on_conflict_statement = insert_statement.on_conflict_do_update(
            set_=data_dict,
            index_elements=index_elements
        ).returning(table.id)

        inserted_id = self.session.execute(on_conflict_statement).scalar()

        self.session.commit()

        return inserted_id

    def upsert_calendar_events_table(self, calendar_event_dict: Dict[str, str]) -> int:
        return self.upsert_into_table(
            CalendarEvent,
            calendar_event_dict,
            [CalendarEvent.host_id, CalendarEvent.host_event_id]
        )

    def upsert_event_hosts_table(self, event_host_dict: Dict[str, str]) -> int:
        return self.upsert_into_table(
            EventHost,
            event_host_dict,
            [EventHost.host_calendar_id]
        )

    @staticmethod
    def fetch_all_data(db_object):
        try:
            data = [item.to_dict() for item in db_object.query.all()]
            print(data)
            return {"success": True, db_object.__tablename__: data}
        except Exception as error:
            return {"success": False, "errors": [str(error)]}

    @staticmethod
    def fetch_single_data(db_object, id):
        try:
            data = db_object.query.get(id).to_dict()
            return {"success": True, db_object.__tablename__[:-1]: data}
        except AttributeError:
            return {"success": False, "errors": [f"{db_object.__name__} item matching {id} not found"]}


db_handler = DBHandler()
