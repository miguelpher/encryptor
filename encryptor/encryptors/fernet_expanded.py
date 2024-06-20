from cryptography.fernet import Fernet
from os import PathLike


class FernetExpanded(Fernet):

    @staticmethod
    def _read_file(filename: str | PathLike) -> bytes:
        with open(filename, "rb") as f:
            data = f.read()
        return data

    @staticmethod
    def _write_file(data: bytes, filename: str | PathLike) -> None:
        with open(filename, "wb") as f:
            f.write(data)

    def encrypt_file(self, input_file: str | PathLike, output_file: str | PathLike):
        original = self._read_file(input_file)
        encrypted_data = super().encrypt(original)
        self._write_file(encrypted_data, output_file)

    def decrypt_file(self, input_file: str | PathLike, output_file: str | PathLike):
        encrypted_data = self._read_file(input_file)
        original_data = super().decrypt(encrypted_data)
        self._write_file(original_data, output_file)
