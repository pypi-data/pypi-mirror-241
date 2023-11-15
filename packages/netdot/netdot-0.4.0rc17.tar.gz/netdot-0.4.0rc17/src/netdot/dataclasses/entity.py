from dataclasses import dataclass
from netdot.csv_util import CSVDataclass
from netdot.dataclasses.base import NetdotAPIDataclass

from netdot import parse


@dataclass
class Entity(NetdotAPIDataclass, CSVDataclass):
    """A BGP Autonomous System."""


    acctnumber: str = None
    aliases: str = None
    asname: str = None
    asnumber: int = None
    availability: str = None
    availability_xlink: int = None
    contactlist: str = None
    contactlist_xlink: int = None
    info: str = None
    maint_contract: str = None
    name: str = None
    oid: str = None
    short_name: str = None
    config_type: str = None


@dataclass
class EntityType(NetdotAPIDataclass, CSVDataclass):

    info: str = None
    name: str = None


@dataclass
class EntityRole(NetdotAPIDataclass, CSVDataclass):
    _xlink_class_map = {"type": "EntityType"}
    _associative_table = True

    entity: str = None
    entity_xlink: int = None
    type: str = None
    type_xlink: int = None


@dataclass
class EntitySite(NetdotAPIDataclass, CSVDataclass):
    _associative_table = True

    entity: str = None
    entity_xlink: int = None
    site: str = None
    site_xlink: int = None
