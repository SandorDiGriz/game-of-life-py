"""File runs the game"""


from game import Game

import argparse
import sys


def main(argv):
    """Takes console arguments and activates the game"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--rows", "-r", help="Number of grid's rows", required=True)
    parser.add_argument(
        "--columns", "-c", help="Number of grid's columns", required=True
    )
    parser.add_argument(
        "--mode",
        "-m",
        help="Mode of cell generation change  ('auto' | 'one-step'), default='auto'",
        default="auto",
    )
    parser.add_argument(
        "--birth_chance",
        "-b",
        help="Percentage probability of a cell being born, default='25'",
        default="25",
    )
    parser.add_argument(
        "--generations_limit",
        "-g",
        help="Maximum number of generations, default='250'",
        default="250",
    )

    args = parser.parse_args(args=argv)

    if args.mode not in ("auto", "one-step"):
        raise argparse.ArgumentTypeError("Invalid game mode: try 'auto' or 'one-step'")

    check_argument(args.rows)
    check_argument(args.columns)
    check_argument(args.birth_chance)
    check_argument(args.generations_limit)

    game = Game(
        rows=int(args.rows),
        columns=int(args.columns),
        mode=args.mode,
        birth_chance=int(args.birth_chance),
        generations_limit=int(args.generations_limit),
    )
    game.run()


def check_argument(arg: str):
    """
    Assures argument is digestible

    Parameters
    ----------
        arg (str): received from the console argument

    Raises
    ----------
        argparse.ArgumentTypeError: if value is numeric must be greater than zero
    """

    if not arg.isnumeric():
        raise argparse.ArgumentTypeError(
            f"Invalid value : {arg}. Try to use numeric value"
        )
    if int(arg) <= 0:
        raise argparse.ArgumentTypeError(
            f"Invalid value : {arg}. Number must be greater than zero"
        )


main(sys.argv[1:])
