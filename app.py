from api import app
from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, snake_case_fallback_resolvers, ObjectType
from ariadne.constants import HTTP_STATUS_200_OK
from flask import request, jsonify
from api.queries import list_calendar_events_resolver, get_calendar_event_resolver, list_event_hosts_resolver, get_event_host_resolver
from api.mutations import upsert_calendar_event_resolver, upsert_event_host_resolver, delete_calendar_event_resolver, delete_event_host_resolver

query = ObjectType("Query")
query.set_field("listCalendarEvents", list_calendar_events_resolver)
query.set_field("getCalendarEvent", get_calendar_event_resolver)
query.set_field("listEventHosts", list_event_hosts_resolver)
query.set_field("getEventHost", get_event_host_resolver)

mutation = ObjectType("Mutation")
mutation.set_field("upsertCalendarEvent", upsert_calendar_event_resolver)
mutation.set_field("upsertEventHost", upsert_event_host_resolver)
mutation.set_field("deleteCalendarEvent", delete_calendar_event_resolver)
mutation.set_field("deleteEventHost", delete_event_host_resolver)

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query, mutation, snake_case_fallback_resolvers
)


@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return HTTP_STATUS_200_OK


@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code
