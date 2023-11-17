"""Tester module for KattisKitten.
"""

from typing import Generator, List
from contextlib import contextmanager
import glob
import time
import sys
import os
from pathlib import Path
from rich.console import Console
from rich.table import Table
# from rich import print
from rich.live import Live
from rich.align import Align
from rich import box

from .utils import utility
from . import config
from .utils import run_python

BEAT_TIME = 0.04


@contextmanager
def beat(length: int = 1) -> Generator[None, None, None]:
    """Beat the heart.

    Args:
        length (int, optional): _description_. Defaults to 1.

    Yields:
        Generator[None, None, None]: yields None
    """
    yield
    time.sleep(length * BEAT_TIME)


def test_samples(
        problemid: str,
        language: str,
        mainclass: str,
        files: List[str],
        ) -> None:
    """Tests a problem by running all the .in files in
    the problem folder and comparing the output to the .ans files.

    Args:
        problem (str): problemid
        log (bool, optional): Defaults to True.

    Returns:
        bool: True if all tests passed, False otherwise.
    """
    console = Console()
    config_data = config.parse_config(language)

    # console.print(extensions)
    # UI Table Header ---

    table = Table(show_header=True,
                  header_style="bold blue",
                  show_lines=True,
                  show_footer=False)
    table.box = box.SQUARE
    table_centered = Align.center(table)

    # End Table Header ---
    # console.print(table)

    # Find all .in files in the problem folder
    if not mainclass:
        mainclass = config_data['mainclass'].replace('<problemid>', problemid)

    curr_dir = Path.cwd()
    root_problem_folder = utility.find_problem_root_folder(curr_dir, problemid)
    if not problemid:
        if root_problem_folder:
            problemid = root_problem_folder.name
        else:
            console.print(
'No problemid specified and I failed to guess \
problemid from filename(s) and current workding dir path.',
        style='bold red')
            sys.exit(1)

    sep = os.path.sep
    in_files = glob.glob(f"{root_problem_folder}{sep}data{sep}*.in")
    in_files.sort()
    # console.print(in_files)
    count = 0
    total = len(in_files)
    console.clear()
    title = f"[not italic bold blue]👷‍ Testing {mainclass} "
    title += f" using {language} 👷‍[/]"
    compiler_error_checked = False
    with Live(table_centered, console=console,
              screen=False, refresh_per_second=20):
        # with beat(10):
        table.title = title
        # with beat(10):
        table.add_column(
            "Input File",
            justify="center",
            style="cyan",
            no_wrap=True)
        table.add_column(
            "Sample Input",
            justify="left",
            style="cyan",
            no_wrap=True)
        table.add_column(
            "Output File",
            justify="center",
            style="cyan",
            no_wrap=True)
        table.add_column(
            "Expected Output",
            justify="left",
            style="cyan",
            no_wrap=True)
        table.add_column(
            "Program Output",
            justify="left",
            style="cyan",
            no_wrap=True)
        table.add_column(
            "Result",
            justify="center",
            style="cyan",
            no_wrap=True)

        for in_file in in_files:
            with open(in_file, 'rb') as f:
                input_content = f.read()
                input_content.replace(b'\r\n', b'\n')  # Windows fix
            out_file = in_file.replace('.in', '.ans')
            with open(out_file, 'rb') as f:
                expected = f.read()
                expected.replace(b'\r\n', b'\n')
            # Run the program
            if language == 'python':
                output = run_python.run(str(mainclass), input_content)
            else:
                raise NotImplementedError(
                    f"Language {language} not supported.")

            expected = expected.strip()

            if expected == output.encode('utf-8').strip():
                result = "[bold green]✅[/bold green]"
                count += 1
            else:
                result = "[bold red]❌[/bold red]"

            # UI Table Row ---
            in_filename = in_file.split('/')[-1]
            out_filename = out_file.split('/')[-1]
            with beat(10):
                table.add_row(in_filename,
                              input_content.decode('utf-8'),
                              out_filename,
                              expected.decode('utf-8'),
                              output,
                              result)
            if not compiler_error_checked:
                compiler_error_checked = True
                if output.startswith('** Syntax Error **'):
                    table.columns[4].style = 'bold red'
                    break

    console.print(f"Total: {count}/{total} tests passed.")
    suggestion = 'Keep trying!' if count < total else \
        'Awesome... Time to submit it to :cat: Kattis! :cat:'
    console.print(suggestion)
