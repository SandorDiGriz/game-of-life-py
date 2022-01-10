import argparse
import sys

from game import Game


def main(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--rows", "-r", help="Number of grid's rows", required=True
    )
    parser.add_argument(
        "--columns", "-c", help="Number of grid's rows", required=True
    )
    parser.add_argument(
        "--mode", "-m", 
        help="Mode of cell generation change  ('auto' | 'one-step'), default='auto'", 
        default="auto"
    )
    parser.add_argument(
        "--birth_chance", "-b", 
        help="Percentage probability of a cell being born, default='25'", 
        default=25
    )
    parser.add_argument(
        "--generations_limit", "-g", 
        help="Maximum number of generations, default='250'", 
        default=250
    )
    
    args = parser.parse_args(args=argv)
    
    if args.mode not in ('auto','one-step'):
        raise argparse.ArgumentTypeError(
            "Invalid game mode: try 'auto' or'one-step'"
        )
    
    game = Game(
        rows=int(args.rows), columns=int(args.columns), mode=args.mode, 
        birth_chance=args.birth_chance, generations_limit=args.generations_limit)
    game.run()
        
main(sys.argv[1:])