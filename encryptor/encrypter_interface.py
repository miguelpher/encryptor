from typing import Protocol
from dataclasses import dataclass
from enum import StrEnum, auto
from pathlib import Path


class Encrypter(Protocol):

    key: str

    @classmethod
    def generate_key(cls) -> bytes:
        ...
    
    def encrypt(self, data: bytes, **kwargs) -> bytes:
        ...

    def decrypt(self, token: bytes, **kwargs) -> bytes:
        ...


class EncryptionMethod(StrEnum):
    FERNET = auto()


class Operation(StrEnum):
    ENCRYPT = auto()
    DECRYIPT = auto()


@dataclass
class Task:
    input_file: str | Path
    output_file: str | Path
    operation: Operation
    key_folder: str | Path
    method: EncryptionMethod

