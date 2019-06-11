import argparse

parser = argparse.ArgumentParser(prog="what")


def start_timer(a):
    print("fisk")


def stop_timer(a):
    print(a)


FUNCTION_MAP = {"start": start_timer}

parser.add_argument("command", choices=FUNCTION_MAP.keys())

args = parser.parse_args()

func = FUNCTION_MAP[args.command]
func()
