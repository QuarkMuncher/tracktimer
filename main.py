import argparse
import sys

parser = argparse.ArgumentParser(prog="what")


def start_timer(a):
    print(a)


def stop_timer():
    print("ksif")


def add_project():
    print("new project!!")


parser.add_argument(
    "--start",
    help="Starts a timer on a project",
    dest="start",
    action="store_true",
)

parser.add_argument(
    "string",
    metavar="S",
    type=str,
    nargs="?",
    help="This is very important, use it right my man",
)

args = parser.parse_args()

# print(args)
# print(sys.argv[-1])

if len(sys.argv) == 1:
    parser.print_help()

if args.start:
    start_timer(args.string)
