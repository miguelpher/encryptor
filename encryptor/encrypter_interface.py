from typing import Protocol
from dataclasses import dataclass
from enum import StrEnum, auto
from pathlib import Path


class Encrypter(Protocol):

    key: str

    @classmethod
    def generate_key(cls) -> bytes: ...

    def encrypt_file(self, input_file: str | Path, output_file: str | Path) -> None: ...

    def decrypt_file(self, input_file: str | Path, output_file: str | Path) -> None: ...


class EncryptionMethod(StrEnum):
    FERNET = auto()


class Operation(StrEnum):
    ENCRYPT = auto()
    DECRYPT = auto()


@dataclass
class Task:
    input_file: str | Path
    output_file: str | Path
    operation: Operation
    key_folder: str | Path
    method: EncryptionMethod
