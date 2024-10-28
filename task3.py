import sys

"""
    This programm provides parsing of log file and return statistic of parsed logs.
    To provides it, program can process arguments of CLI, where first arg is path to log file and second - level of processing
    Processing provides by using functions:
    function parse_log_line - parses lines of log file and return result as a dictionary
    function load_logs - Get inputed path to log file as argument, loads logs from its file and return list of dictionaries.
    function filter_logs_by_level - filters logs by level and return list of logs, that match to the request.
    function count_logs_by_level - provide counting of logs that match to parsed levels.
    function display_log_counts - prints to console results of log analizing.
    
"""


def parse_log_line(line: str) -> dict:

    date, time, level, message = line.split(" ", 3)
    return {"time": str(date) + str(time), "level": level, "message": message}


def load_logs(file_path: str) -> list:

    with open(file_path, "r") as f:
        logs = [parse_log_line(line) for line in f]
    return logs


def filter_logs_by_level(logs: list, level: str) -> list:

    return [log for log in logs if log["level"] == level.upper()]


def count_logs_by_level(logs: list) -> dict:

    counts = {}
    for log in logs:
        counts[log["level"]] = counts.get(log["level"], 0) + 1
    return counts


def display_log_counts(counts: dict):

    print("Результати аналізу логів:")
    for level, count in counts.items():
        print(f"{level}: {count}")


def main():
    args = sys.argv
    log_file = None
    level = None
    if len(args) > 3 or len(args) == 1:
        log_file = input("input path to log file: ")
    elif len(args) == 3:
        log_file = args[1]
        level = args[2]
    else:
        log_file = args[1]

    logs = load_logs(log_file)

    if level:
        filtered_logs = filter_logs_by_level(logs, level)
        counts = count_logs_by_level(filtered_logs)
    else:
        counts = count_logs_by_level(logs)

    display_log_counts(counts)
    if level:
        for items in filtered_logs:
            print(f"{items['time']} {items['message']}", end="")


if __name__ == "__main__":
    main()
