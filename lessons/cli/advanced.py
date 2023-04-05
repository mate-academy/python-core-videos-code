from cli.run import run
from cli.default import default_operations
from calculator.advanced import floor_divide, modulo

advanced_operations = dict(default_operations, floor_divide=floor_divide, modulo=modulo)


def run_advanced_cli():
    run(advanced_operations)
