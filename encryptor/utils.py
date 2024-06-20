from enum import StrEnum
from .encryptors import FernetExpanded

from .encrypter_interface import EncryptionMethod, Encrypter, Operation


def _parse_str_enum(some_str: str, my_enum: StrEnum):
    try:
        return my_enum(some_str.lower())
    except ValueError as e:
        print(f"{my_enum.__name__} '{some_str}' not supported")
        raise e


def get_parsed_operation(operation_str) -> Operation:
    return _parse_str_enum(operation_str, Operation)


def get_parsed_method(method_str) -> EncryptionMethod:
    return _parse_str_enum(method_str, EncryptionMethod)


def load_encryption_method(method: EncryptionMethod) -> Encrypter:
    match method:
        case EncryptionMethod.FERNET:
            return FernetExpanded
        case _:
            raise ValueError("Encryption method not supported")
