from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from api import db


class EventHost(db.Model):
    __tablename__ = 'event_hosts'
    id = Column(Integer(), primary_key=True,  autoincrement=True)
    host_calendar_id = Column(String(100), index=True, unique=True)
    host_name = Column(String(100))
    host_description = Column(String(1000))
    host_website = Column(String(100))
    host_email = Column(String(100))
    events = relationship('CalendarEvent')

    def to_dict(self):
        return {
            "id": self.id,
            "host_calendar_id": self.host_calendar_id,
            "host_name": self.host_name,
            "host_description": self.host_description,
            "host_website": self.host_website,
            "host_email": self.host_email,
            "events": [event.to_dict() for event in self.events]
        }


class CalendarEvent(db.Model):
    __tablename__ = 'calendar_events'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    host_id = Column(Integer(), ForeignKey('event_hosts.id'))
    host_event_id = Column(String(100))
    event_name = Column(String(100))
    event_description = Column(String(300))
    event_price = Column(Integer())
    event_start_date = Column(DateTime())
    event_end_date = Column(DateTime())
    event_location = Column(String(100))

    def to_dict(self):
        return {
            "id": self.id,
            "host_id": self.host_id,
            "host_event_id": self.host_event_id,
            "event_name": self.event_name,
            "event_description": self.event_description,
            "event_price": self.event_price,
            "event_start_date": str(self.event_start_date.strftime('%d-%m-%Y')),
            "event_end_date": str(self.event_end_date.strftime('%d-%m-%Y')),
            "event_location": self.event_location
        }
