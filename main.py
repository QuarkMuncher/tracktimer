import argparse
import sys

parser = argparse.ArgumentParser(prog="what")


def start_timer():
    print("fisk")


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

args = parser.parse_args()

# print(args)
# print(sys.argv[-1])

if len(sys.argv) == 1:
    parser.print_help()

if args.start:
    print("whoo")
