from dataclasses import dataclass
from enum import StrEnum, auto
from pathlib import Path


KEY_FORMAT = "{}.key"
KEY_FOLDER = Path.home() / ".encrypter"


class EncryptionMethod(StrEnum):
    FERNET = auto()


def get_key_path(method: EncryptionMethod) -> str:
    return KEY_FORMAT.format(method)


class Operation(StrEnum):
    ENCRYPT = auto()
    DECRYIPT = auto()


@dataclass
class Task:
    input_file: str | Path
    output_file: str | Path
    operation: Operation
    key_folder: str | Path
