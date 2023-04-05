from calculator.default import add, subtract, multiply, divide
from .run import run

default_operations = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
}


def run_default_cli():
    run(default_operations)

