from __future__ import annotations

from uuid import UUID
import datetime
from enum import Enum
from typing import Any, Literal

from pydantic import BaseModel, UUID1, UUID3, UUID4, UUID5


class PaymentCardBrand(Enum):
    AMERICAN_EXPRESS = "American Express"
    MASTERCARD = "Mastercard"
    VISA = "Visa"
    MIR = "Mir"
    OTHER = "other"


class Flavor(Enum):
    MOCHA = "mocha"
    VANILLA = "vanilla"
    PEPPERMINT = "peppermint"


class Numbers(Enum):
    NUMBER_1 = 1
    NUMBER_2 = 2
    NUMBER_3 = 3


class Vector3(BaseModel):
    x: float
    y: float
    z: float


class PydanticTypes(BaseModel):
    strict_bool: bool
    positive_int: int
    negative_int: int
    non_positive_int: int
    non_negative_int: int
    strict_int: int
    positive_float: float
    negative_float: float
    non_positive_float: float
    non_negative_float: float
    strict_float: float
    finite_float: float
    strict_bytes: bytes
    strict_str: str
    uuid1: UUID1
    uuid3: UUID3
    uuid4: UUID4
    uuid5: UUID5
    base64_bytes: str
    base64_str: str
    str_constraints_strip_whitespace: str
    str_constraints_to_upper: str
    str_constraints_to_lower: str
    str_constraints_strict: str
    str_constraints_min_length: str
    str_constraints_max_length: str
    json_field: str
    past_date: datetime.date
    future_date: datetime.date
    aware_datetime: datetime.datetime
    naive_datetime: datetime.datetime
    past_datetime: datetime.datetime
    future_datetime: datetime.datetime
    constrained_float: float


class PydanticNetworkTypes(BaseModel):
    any_url: str
    any_http_url: str
    http_url: str
    postgres_dsn: str
    cockroach_dsn: str
    amqp_dsn: str
    redis_dsn: str
    mongo_dsn: str
    kafka_dsn: str
    mysql_dsn: str
    mariadb_dsn: str
    email_str: str
    name_email: str
    ipv_any_address: str
    ipv_any_interface: str
    ipv_any_network: str


class PydanticExtra(BaseModel):
    color: str
    payment_card_brand: PaymentCardBrand
    payment_card_number: str
    aba_routing_number: str


class KineticBody(BaseModel):
    position: Vector3
    velocity: Vector3
    mass: float


class VanillaModel(BaseModel):
    bool_field: bool


class RecursiveModel(BaseModel):
    value: int
    child: RecursiveModel | None


class Constantly(BaseModel):
    const_str_field: Literal["Cat."]
    const_num_field: Literal[3]
    const_none_field: Literal[None]
    const_true_field: Literal[True]
    const_false_field: Literal[False]


class Primitives(BaseModel):
    int_field: int
    float_field: float
    str_field: str
    bool_field: bool
    bytes_field: bytes
    none_field: None


class PythonTypes(BaseModel):
    str_enum: Flavor
    num_enum: Numbers
    date: datetime.date
    time: datetime.time
    datetime_field: datetime.datetime
    timedelta: datetime.timedelta
    uuid_field: UUID
    decimal: float | str
    path: str


class DefaultFactory(BaseModel):
    id: UUID


class Defaults(BaseModel):
    str_field: str
    int_field: int
    float_field: float
    bool_true: bool
    bool_false: bool
    list_field: list[str] | None
    child_field: DefaultFactory | None


class CollectionsModel(BaseModel):
    list_field: list[Any]
    list_str: list[str]
    list_list: list[list[Any]]
    list_list_int: list[list[int]]
    list_model: list[VanillaModel]
    list_model_or_model: list[VanillaModel | RecursiveModel]
    list_union: list[str | int]
    list_dict: list[dict[str, Any]]
    list_dict_str: list[dict[str, str]]
    list_dict_int_keys: list[dict[str, str]]
    tuple_field: list[Any]
    tuple_str: tuple[str]
    tuple_tuple: tuple[list[Any]]
    tuple_tuple_int: tuple[tuple[int]]
    tuple_model: tuple[VanillaModel]
    tuple_union: tuple[str | int]
    tuple_int_str_none: tuple[int, str, None]
    set_str: set[str]
    set_union: set[str | int]
    dict_field: dict[str, Any]
    dict_str: dict[str, str]
    dict_dict: dict[str, dict[str, Any]]
    dict_int_keys: dict[str, str]
    dict_model: dict[str, VanillaModel]
    dict_model_or_model: dict[str, VanillaModel | RecursiveModel]
    dict_union: dict[str, str | int]
    dict_list: dict[str, list[int]]


class ConstrainedCollections(BaseModel):
    list_min: list[Any]
    list_max: list[str]
    list_min_max: list[str]
