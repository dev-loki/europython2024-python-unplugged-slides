from typing import TypedDict, NotRequired, Required


class SomeWebresponse(TypedDict):
    message: str
    status_code: int
    errors: NotRequired[list[str]]


class SomeOtherWebResponse(TypedDict, total=False):
    message: Required[str]
    status_code: Required[int]
    errors: list[str]
