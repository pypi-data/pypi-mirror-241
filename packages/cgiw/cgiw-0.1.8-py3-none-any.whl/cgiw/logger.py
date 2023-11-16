from os.path import isfile, join
from os import getenv
from datetime import datetime


log_directory = getenv("LOG_DIRECTORY", "./")
log_file_name = getenv("LOG_FILE_NAME", "log.txt")

log_file_path = join(log_directory, log_file_name)


if not isfile(log_file_path):
    open(log_file_path, "x").close()

log_file = open(log_file_path, "a")


def log(message: str):
    log_file.write(f"{datetime.now()} - {message} \n")
