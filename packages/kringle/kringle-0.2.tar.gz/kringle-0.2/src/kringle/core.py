from importlib.machinery import SourceFileLoader
from inspect import Signature, signature
from pathlib import Path
from types import ModuleType
from typing import Any, Callable


def _run_part(solution: ModuleType, part: int, data: Any) -> None:
    """
    Run the specified part of the solution.

    Args:
        part (int): The part to run.
        data (Any): The data to pass to the solution.
    """
    func: Callable = getattr(solution, f"part_{part}")
    sig: Signature = signature(func)
    if len(sig.parameters) == 0:
        print(f"Part {part}: ", func())  # noqa: T201
    else:
        print(f"Part {part}: ", func(data))  # noqa: T201


def run() -> None:
    """Run both parts of a solution, displaying their results."""

    # Load the solution module
    module_path: str = str(Path.cwd() / "solution.py")
    loader: SourceFileLoader = SourceFileLoader("solution", module_path)
    solution: ModuleType = loader.load_module()

    # Parse the data for the module
    with open("input.txt") as f:
        data: Any = solution.parse(f.read())

    _run_part(solution, 1, data)
    _run_part(solution, 2, data)
