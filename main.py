import argparse
import json
from datetime import datetime

from scheduler.core import Scheduler


def parse_time(time_str: str) -> float:
    """Parse ISO formatted time string to epoch seconds."""
    return datetime.fromisoformat(time_str).timestamp()


def main():
    parser = argparse.ArgumentParser(description="Simple scheduler")
    parser.add_argument("file", help="JSON file with tasks")
    args = parser.parse_args()

    sched = Scheduler()
    with open(args.file) as f:
        tasks = json.load(f)

    for task in tasks:
        run_at = parse_time(task["time"])
        message = task["message"]
        sched.schedule_at(run_at, print, (message,))

    sched.run()


if __name__ == "__main__":
    main()
