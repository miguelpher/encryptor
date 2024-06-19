import click
from .encrypter_interface import Task, Encrypter, Operation
from .key_manager import KEY_FOLDER, KeyManager
from .utils import load_encryption_method, get_parsed_operation, get_parsed_method


def init_encrypter(method, key_folder) -> Encrypter:
    encrypter = load_encryption_method(method)
    key_manager = KeyManager(key_folder, method)
    return encrypter(key_manager.get_key())


def process_task(task: Task,):
    encrypter = init_encrypter(task.method, task.key_folder)
    match task.operation:
        case Operation.ENCRYPT:
            pass
        case Operation.DECRYIPT:
            pass
        case _:
            raise ValueError(f"Operation {task.operation} not feasible")


@click.command()
@click.argument("operation")
@click.argument("input_filepath", type=click.Path(exists=True))
@click.argument("output_filepath", type=click.Path(exists=False))
@click.option("-k", "--key-folder", type=str, default=KEY_FOLDER, help=f"{KEY_FOLDER} by default")
@click.option("-m", "--method", type=str, default="fernet", help=f"Encryption method. Only fernet supported in this version")
def cli(operation: str, input_filepath: str, output_filepath: str, key_folder: str, method: str) -> Task:
    """Encrypt or decrypt a file and write the result to another file\n
    OPERATION: encrypt | decrypt\n
    INPUT_FILEPATH: any filepath that exists\n
    OUTPUT_FILEPATH any output filepath. If exists, it will be overwritten\n
    """
    task = Task(
        input_file=input_filepath,
        output_file=output_filepath,
        operation=get_parsed_operation(operation),
        key_folder=key_folder,
        method=get_parsed_method(method),
    )
    process_task(task)
