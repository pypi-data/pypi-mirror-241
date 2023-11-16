#!/usr/bin/env python3
import argparse
import sys
from datetime import datetime, timedelta
import tomlkit
import os
import logging

logger = logging.getLogger("newold")

def parse_args():
    parser = argparse.ArgumentParser(
        description="Print only new values to stdout, or those that weren't seen in a while."
    )

    parser.add_argument(
        "target",
        help="string or file with lines to process. "
        "If none then stdin will be use",
        nargs="*",
    )

    parser.add_argument(
        "--db",
        metavar="PATH",
        help="Specify db file. NEWOLD_DB environment variable can also be used.",
    )

    parser.add_argument(
        "-s", "--seconds",
        help="Seconds that must pass",
        type=int,
    )

    parser.add_argument(
        "-m", "--minutes",
        help="Minutes that must pass",
        type=int
    )

    parser.add_argument(
        "-H", "--hours",
        help="Hours that must pass",
        type=int
    )

    parser.add_argument(
        "-d", "--days",
        help="Days that must pass",
        type=int
    )

    parser.add_argument(
        "--verbose",
        "-v",
        action="count",
        help="Verbosity",
        default=0
    )

    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    init_log(args.verbose)

    if args.db is not None:
        db_file = args.db
    else:
        db_file = os.getenv("NEWOLD_DB")

    if not db_file:
        logger.info(
            "Database file not specified. Targets won't be saved."\
            " Use --db param or NEWOLD_DB environment variable to set database."
        )

    logger.info("Database file: '%s'", db_file)
    min_delta = calculate_delta(
        seconds=args.seconds,
        minutes=args.minutes,
        hours=args.hours,
        days=args.days,
    )

    db = create_db(db_file)
    try:
        process_lines(db, args.target, min_delta)
    except (KeyboardInterrupt, BrokenPipeError):
        pass
    finally:
        db.save_db()

def process_lines(db, targets, min_delta):
    now_dt = datetime.now()

    for line in read_text_targets(targets):
        try:
            dt = db.get_target(line)
            delta = now_dt - dt
            if delta < min_delta:
                continue
        except KeyError:
            pass

        db.add_target(line, now_dt)
        print(line)

def init_log(verbosity=0, log_file=None):

    if verbosity == 0:
        level = logging.WARN
    elif verbosity == 1:
        level = logging.INFO
    elif verbosity > 1:
        level = logging.DEBUG
    else:
        level = logging.CRITICAL

    logging.basicConfig(
        level=level,
        filename=log_file,
        format="%(levelname)s:%(name)s:%(message)s"
    )


def calculate_delta(seconds=None, minutes=None, hours=None, days=None):
    specified = False
    if seconds is not None\
       or minutes is not None\
       or hours is not None\
       or days is not None:
        specified = True

    if specified:
        seconds = seconds or 0
        minutes = minutes or 0
        hours = hours or 0
        days = days or 0
        return timedelta(
            seconds=seconds,
            minutes=minutes,
            hours=hours,
            days=days
        )
    else:
        return timedelta.max

def create_db(db_file):
    if not db_file:
        return MemoryDb(db_file)
    return TomlDb(db_file)

class Db:

    def __init__(self, db_file):
        self.db_file = db_file
        self.db = self._load_db(db_file)

    def _load_db(self, db_file):
        raise NotImplementedError()

    def get_target(self, target):
        return self.db[target]

    def add_target(self, target, date):
        self.db[target] = date

    def save_db(self):
        raise NotImplementedError()

class TomlDb(Db):

    def _load_db(self, db_file):
        try:
            with open(db_file) as fi:
                return tomlkit.load(fi)
        except FileNotFoundError:
            logger.info("Database file not found. An empty database will be used.")
            return {}

    def save_db(self):
        with open(self.db_file, "w") as fo:
            tomlkit.dump(self.db, fo)

class MemoryDb(Db):

    def _load_db(self, _):
        return {}

    def save_db(self):
        return



def read_text_targets(targets):
    yield from read_text_lines(read_targets(targets))


def read_targets(targets):
    """Function to process the program ouput that allows to read an array
    of strings or lines of a file in a standard way. In case nothing is
    provided, input will be taken from stdin.
    """
    if not targets:
        yield from sys.stdin

    for target in targets:
        try:
            with open(target) as fi:
                yield from fi
        except FileNotFoundError:
            yield target


def read_text_lines(fd):
    """To read lines from a file and skip empty lines or those commented
    (starting by #)
    """
    for line in fd:
        line = line.strip()
        if line == "":
            continue
        if line.startswith("#"):
            continue

        yield line


if __name__ == '__main__':
    main()
