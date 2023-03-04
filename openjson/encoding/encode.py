# External class visibility
__all__ = ['_encode_object', '_encode_array', '_encode_number_int', '_encode_number_real', '_encode_string', '_encode_boolean', '_encode_null', '_encode']


def _encode_object(key: str, value: dict):
    string = f"\"{key}\": " + "{"
    for index, item in enumerate(value):
        if index != len(value) - 1:
            string += f"{_encode(item, value[item])}, "
        else:
            string += f"{_encode(item, value[item])}"
    string += "}"
    return string


def _encode_array(key: str, value: list):
    string = f"\"{key}\": ["
    for index, item in enumerate(value):
        if index != len(value) - 1:
            string += f"\"{item}\", "
        else:
            string += f"\"{item}\""
    string += "]"
    return string


def _encode_number_int(key: str, value: int):
    return f"\"{key}\": {value}"


def _encode_number_real(key: str, value: int, precision: float = None):
    if precision is not None:
        return f"\"{key}\": {round(value, precision)}"
    else:
        return f"\"{key}\": {value}"


def _encode_string(key: str, value: str):
    return f"\"{key}\": \"{value}\""


def _encode_boolean(key: str, value: bool):
    if value is True:
        return f"\"{key}\": true"
    if value is False:
        return f"\"{key}\": false"
    

def _encode_null(key: str):
    return f"\"{key}\": null"


def _encode(key: str, value: object, int_precision: int = None) -> str:
    match type(value).__name__:
        case "dict":
            return _encode_object(key=key, value=value)
        case "list":
            return _encode_array(key=key, value=value)
        case "int":
            return _encode_number_int(key=key, value=value)
        case "float":
            return _encode_number_real(key=key, value=value, precision=int_precision)
        case "str":
            return _encode_string(key=key, value=value)
        case "bool":
            return _encode_boolean(key=key, value=value)            
        case "NoneType":
            return _encode_null(key=key)
        case other:
            raise NotImplementedError(f"Type \"{other}\" is not supported.")
