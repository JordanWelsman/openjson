from openjson.encoding import _encode

__all__ = ['stringify']

def stringify(object: dict) -> str:
    string: str = "{"
    for index, item in enumerate(object):
        if index != len(object) - 1:
            string += f"{_encode(key=item, value=object[item])}, "
        else:
            string += f"{_encode(key=item, value=object[item])}"

    string += "}"
    return string