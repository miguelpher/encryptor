import os
from pathlib import Path
from .encrypter_interface import EncryptionMethod
from .utils import load_encryption_method

KEY_FORMAT = "{}.key"
KEY_FOLDER = Path.home() / ".encrypter"

class KeyManager:

    def __init__(self, key_folder: os.PathLike, encryption_method: EncryptionMethod) -> None:
        self.key_folder = Path(key_folder)
        self.encryption_method = encryption_method

    @property
    def key_path(self) -> Path:
        return self.key_folder / KEY_FORMAT.format(self.encryption_method)

    def generate_key(self):
        encrypter = load_encryption_method(self.encryption_method)
        return encrypter.generate_key()

    def write_key(self, key: bytes) -> None:
        os.makedirs(self.key_folder, exist_ok=True)
        with open(self.key_path, "wb") as mykey:
            mykey.write(key)

    def load_key(self) -> bytes:
        with open(self.key_path, "rb") as mykey:
            key = mykey.read()
        return key

    def get_key(self) -> bytes:
        try:
            return self.load_key()
        except FileNotFoundError:
            user_input = input(f"No encryption key found (looking at {self.key_path}), would you like yo create one? (y/n)")
            if user_input.lower() in ["yes", "y"]:
                self.write_key()
                return self.load_key()
            else:
                print("Exiting...")
                exit(0)
