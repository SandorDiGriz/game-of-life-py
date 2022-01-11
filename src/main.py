"""File runs the game"""


import argparse
import sys

from game import Game


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
        default=25,
    )
    parser.add_argument(
        "--generations_limit",
        "-g",
        help="Maximum number of generations, default='250'",
        default=250,
    )

    args = parser.parse_args(args=argv)

    if args.mode not in ("auto", "one-step"):
        raise argparse.ArgumentTypeError("Invalid game mode: try 'auto' or 'one-step'")

    if args.birth_chance:
        try:
            int(args.birth_chance)
        except ValueError:
            raise argparse.ArgumentTypeError(
                "Invalid probability of a cell birth: try to use numeric value"
            )

    if args.generations_limit:
        try:
            int(args.generations_limit)
        except ValueError:
            raise argparse.ArgumentTypeError(
                "Invalid limit of generations: try to use numeric value"
            )

    game = Game(
        rows=int(args.rows),
        columns=int(args.columns),
        mode=args.mode,
        birth_chance=int(args.birth_chance),
        generations_limit=int(args.generations_limit),
    )
    game.run()


main(sys.argv[1:])
