# Scheduler

This repository provides a minimal task scheduler written in Python. It uses the
built-in `sched` module to run tasks at specific times.

## Usage

Add tasks to a JSON file. Each entry should contain an ISO formatted `time` and a
`message` to print when the task runs.

Example `tasks.json`:

```json
[
  {"time": "2024-01-01T00:00:00", "message": "Happy New Year!"}
]
```

Run the scheduler with:

```bash
python main.py tasks.json
```

### Excel assignment scheduler

If you work with Excel files, the `scheduler/excel.py` module provides a script
that replicates the scheduling logic from the example Office Script. It assigns
teams to the next available business days while skipping blackout weeks.

Usage:

```bash
python -m scheduler.excel path/to/workbook.xlsx
```

The script requires `openpyxl` to be installed.

## Testing

Run unit tests with:

```bash
python -m pytest -q
```

