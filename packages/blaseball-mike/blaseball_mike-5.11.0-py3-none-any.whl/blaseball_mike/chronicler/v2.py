"""
Chronicler V2 Endpoints
"""
from .chron_helpers import prepare_id, paged_get
from datetime import datetime
from blaseball_mike.session import session, check_network_response, TIMESTAMP_FORMAT

BASE_URL_V2 = 'https://api.sibr.dev/chronicler/v2'

"""List of Types:
* player
* team
* stream
* game
* idols
* tributes
* temporal
* tiebreakers
* sim
* globalevents
* offseasonsetup
* standings
* season
* league
* subleague
* division
* gamestatsheet
* teamstatsheet
* playerstatsheet
* seasonstatsheet
* bossfight
* offseasonrecap
* bonusresult
* decreeresult
* eventresult
* playoffs
* playoffround
* playoffmatchup
* tournament
* stadium
* renovationprogress
* teamelectionstats
"""


# WRAPPER FUNCTIONS

def get_entities(type_, id_=None, at=None, count=None, page_size=1000, cache_time=5):
    """
    Chronicler V2 Entities endpoint
    Returns list of all entities of a certain type at one point in time

    Args:
        type_: type of entity to filter by (player, team, etc)
        id_: id or list of ids to filter type by
        at: return entities at this timestamp
        count: number of entries to return.
        page_size: number of elements to get per-page
        cache_time: response cache lifetime in seconds, or `None` for infinite cache
    """
    if isinstance(at, datetime):
        at = at.strftime(TIMESTAMP_FORMAT)

    params = {"type": type_}
    if id_:
        params["id"] = prepare_id(id_)
    if at:
        params["at"] = at
    if count:
        params["count"] = count

    s = session(cache_time)
    if page_size:
        if page_size < 1 or page_size > 1000:
            raise ValueError("page_size must be between 1 and 1000")
        params["count"] = page_size

    s = session(cache_time)
    return paged_get(f'{BASE_URL_V2}/entities', params=params, session=s, total_count=count, page_size=page_size, lazy=True)


def get_versions(type_, id_=None, before=None, after=None, order=None, count=None, page_size=1000, cache_time=5):
    """
    Chronicler V2 Versions endpoint
    Returns generator of changes to entities over time

    Args:
        type_: type of entity to filter by (player, team, etc)
        id_: id or list of ids to filter type by
        before: return elements before this string or datetime timestamp.
        after: return elements after this string or datetime timestamp.
        order: sort in ascending ('asc') or descending ('desc') order.
        count: number of entries to return.
        page_size: number of elements to get per-page
        cache_time: response cache lifetime in seconds, or `None` for infinite cache
    """
    if isinstance(before, datetime):
        before = before.strftime(TIMESTAMP_FORMAT)
    if isinstance(after, datetime):
        after = after.strftime(TIMESTAMP_FORMAT)

    params = {"type": type_}
    if id_:
        params["id"] = prepare_id(id_)
    if before:
        params["before"] = before
    if after:
        params["after"] = after
    if order:
        if order.lower() not in ('asc', 'desc'):
            raise ValueError("Order must be 'asc' or 'desc'")
        params["order"] = order
    if page_size:
        if page_size < 1 or page_size > 1000:
            raise ValueError("page_size must be between 1 and 1000")
        params["count"] = page_size

    s = session(cache_time)
    return paged_get(f'{BASE_URL_V2}/versions', params=params, session=s, total_count=count, page_size=page_size, lazy=True)
