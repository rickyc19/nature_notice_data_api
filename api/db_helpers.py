from sqlalchemy.dialects.postgresql import insert
from api import db


def upsert_into_table(table, data_dict, index_elements) -> int:
    insert_statement = insert(table).values(data_dict)

    on_conflict_statement = insert_statement.on_conflict_do_update(
        set_=data_dict,
        index_elements=index_elements
    ).returning(table.id)

    inserted_id = db.session.execute(on_conflict_statement).scalar()
    db.session.commit()

    return inserted_id


def fetch_all_entry(db_object):
    try:
        entry = [item.to_dict() for item in db_object.query.all()]
        return {"success": True, db_object.__tablename__: entry}
    except Exception as error:
        return {"success": False, "errors": [str(error)]}


def fetch_single_entry(db_object, id):
    try:
        entry = db_object.query.get(id).to_dict()
        return {"success": True, db_object.__tablename__[:-1]: entry}
    except AttributeError:
        return {"success": False, "errors": [f"{db_object.__name__} item matching {id} not found"]}


def delete_entry(db_object, id):
    try:
        entry = db_object.query.get(id)
        db.session.delete(entry)
        db.session.commit()
        return {"success": True, db_object.__tablename__[:-1]: entry}
    except AttributeError:
        return {"success": False, "errors": [f"{db_object.__name__} item matching {id} not found"]}
