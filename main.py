import argparse
import sys
import database as db

parser = argparse.ArgumentParser(prog="what")


def start_timer(a):
    db.start_timer(a)


def stop_timer():
    print("ksif")


def new_project(a):
    print(db.insert_project(a))


def list_projects():
    for p in db.find_projects():
        print(p)


parser.add_argument(
    "--start",
    help="starts a project like this: --start 'project name'",
    dest="start",
    action="store_true",
)

parser.add_argument(
    "--stop",
    help="Stops the currently running timer.",
    dest="stop",
    action="store_true",
)

parser.add_argument(
    "--new",
    help="Add a new project like this: --new 'new project name'",
    dest="new",
    action="store_true",
)

parser.add_argument(
    "--list",
    help="Lists all projects currently in db.",
    dest="list",
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
    try:
        if len(args.string) > 2:
            start_timer(args.string)
        else:
            print("Name too short")
    except Exception as e:
        print(e)
        parser.print_help()
if args.stop:
    stop_timer()
if args.new:
    try:
        if len(args.string) > 2:
            new_project(args.string)
        else:
            print("Name too short")
    except Exception:
        parser.print_help()
if args.list:
    list_projects()
