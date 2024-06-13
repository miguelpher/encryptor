import click
from .static_tools import Task, KEY_FOLDER


def process_task(task: Task):
    print(task)


@click.command()
@click.argument("operation")
@click.argument("input_filepath", type=click.Path(exists=True))
@click.argument("output_filepath", type=click.Path(exists=False))
@click.option("-k", "--key-folder", type=str, default=KEY_FOLDER, help=f"{KEY_FOLDER} by default")
def cli(operation: str, input_filepath, output_filepath, key_folder) -> Task:
    """Encrypt or decrypt a file and write the result to another file\n
    OPERATION: encrypt | decrypt\n
    INPUT_FILEPATH: any filepath that exists\n
    OUTPUT_FILEPATH any output filepath. If exists, it will be overwritten\n

    """
    task = Task(
        input_file=input_filepath,
        output_file=output_filepath,
        operation=operation,
        key_folder=key_folder,
    )
    process_task(task)
