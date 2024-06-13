from pathlib import Path
from .static_tools import EncryptionMethod
from cryptography.fernet import Fernet


class KeyManager:

    def generate_key(self, encryption_method: EncryptionMethod):
        match encryption_method:
            case EncryptionMethod.FERNET:
                return Fernet.generate_key()
            case _:
                raise ValueError("Encryption method not supported")

    def write_key(self, key, key_path):
        with open(key_path, "wb") as mykey:
            mykey.write(key)

    def load_key(self, key_path: str | Path):
        with open(key_path, "rb") as mykey:
            key = mykey.read()
        return key
