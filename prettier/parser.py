from typing import Any, TYPE_CHECKING

from .models import settings

if TYPE_CHECKING:
    from models import settings

## --Variables-- ##
default_settings = settings()

## --Methods-- ##


def parse_dictionary(data: dict[str, Any], colors: settings = default_settings) -> str:
    index = 0
    buffer = f"{colors.dictionary}{{{colors.reset}"

    for key, value in data.items():
        index += 1
        buffer += f'{colors.string}"{key}"{colors.reset}{colors.dictionary}: {colors.reset}'
        buffer += parse(value, colors=colors)

        if not index == len(data):
            buffer += f"{colors.array}, {colors.reset}"

    buffer += f"{colors.dictionary}}}{colors.reset}"

    return buffer


def parse_list(data: list[Any], colors: settings = default_settings) -> str:
    buffer = f"{colors.array}[{colors.reset}"

    for index, value in enumerate(data):
        index += 1
        buffer += parse(value, colors=colors)

        if not index == len(data):
            buffer += f"{colors.array}, {colors.reset}"

    buffer += f"{colors.array}]{colors.reset}"

    return buffer


def parse(data: Any, colors: settings = default_settings) -> str:
    if isinstance(data, str):
        return f'{colors.string}"{data}"{colors.reset}'

    if isinstance(data, int):
        return f"{colors.integer}{data}{colors.reset}"

    if isinstance(data, float):
        return f"{colors.decimal}{data}{colors.reset}"

    if isinstance(data, bool):
        return f"{colors.boolean}{data}{colors.reset}"

    if data is None:
        return f"{colors.boolean}null{colors.reset}"

    if isinstance(data, list):
        return parse_list(data, colors=colors)

    if isinstance(data, dict):
        return parse_dictionary(data, colors=colors)

    raise TypeError(f"Object of type {data.__class__.__name__} is not JSON serializable.")
