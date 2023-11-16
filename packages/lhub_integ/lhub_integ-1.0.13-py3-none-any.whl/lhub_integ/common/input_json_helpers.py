import json
import os
import sys

from lhub_integ.common.input_helpers import _get_stripped_env_string
from lhub_integ.common.constants import INPUT_DATA_JSON_FOLDER_PATH, OUTPUT_DATA_JSON_FILE_PATH

file_writer = None


def convert_input(rows, input_converter):
    """
    rows: A generator whose row needs to be transformed independently by the function `input_converter`
    """
    for row in rows:
        yield input_converter(row)


def get_input_data():
    """
    This is the main function which return the Input DataFrame Iterator.
    It either returns
        - A list when Pipe IO is used
        - A generator when File IO is used
    """
    input_data_file_path = _get_stripped_env_string(INPUT_DATA_JSON_FOLDER_PATH)
    if input_data_file_path:
        return get_input_from_text_file(input_data_file_path)
    else:
        return sys.stdin.readlines()


def parse_row_as_dict(row):
    """
    Before Every row data was inside this field 'row' which won't be there anymore in File IO.
    """
    parsed_json = json.loads(row)
    if _get_stripped_env_string(INPUT_DATA_JSON_FOLDER_PATH):
        return parsed_json
    else:
        return parsed_json['row']


def __get_input_file_path(folder_path):
    path_exists = os.path.exists(folder_path)
    folder_exists = os.path.isdir(folder_path)
    # Path should exist and should be a directory.
    if not path_exists or not folder_exists:
        return None
    # Take all files starting with part in the directory.
    files = [file_name for file_name in os.listdir(folder_path) if file_name.startswith('part')]
    if len(files) == 0:
        return None
    return folder_path.strip() + '/' + files[0]


# Once an iterators __next__() method raises StopIteration, it must continue to do so on subsequent calls.
# Implementations that do not obey this property are deemed broken.
def get_input_from_text_file(json_input_folder_path):
    file_path = __get_input_file_path(json_input_folder_path)
    # If file is not found then simply return so that generator completes
    if file_path is None:
        return
    f = open(file_path, 'r', encoding='utf-8')
    try:
        with f:
            for row in f:
                yield row
    finally:
        f.close()


class JsonFileIO:
    f = None
    output = []

    def __init__(self):
        output_path = _get_stripped_env_string(OUTPUT_DATA_JSON_FILE_PATH)
        self.f = open(output_path, 'wb')

    def __del__(self):
        self.handle_aftermath()

    def handle_aftermath(self):
        """
        All output after last result are discarded and the output file is closed.
        """
        if self.f is not None:
            self.f.close()

    def write_stderr(self, msg):
        self.write_output(stderr=msg)

    def write_stdout(self, msg):
        self.write_output(stdout=msg)

    def write_output(self, result=None, original_lhub_id=None, stdout="", stderr=""):
        """
        When something is given to print store it and flush if the latest entry has result.
        """
        self.output.append((result, original_lhub_id, stdout, stderr))
        if result:
            self.flush()

    def flush(self):
        res = self.output
        original_lhub_ids = list(set(i[1] for i in res if i[1] is not None))
        if len(original_lhub_ids) == 1:
            original_lhub_id = original_lhub_ids[0]
        else:
            original_lhub_id = None
        merged_stdout = "\n".join([i[2] for i in res if i[2]])
        merged_stderr = "\n".join([i[3] for i in res if i[3]])
        results = list(i[0] for i in res if i[0])
        result = results[0] if len(results) == 1 else results
        self.output = []
        output_row = json.dumps({
            'result': result,
            'stdout': merged_stdout,
            'stderr': merged_stderr,
            'original_lhub_id': original_lhub_id
        })
        output_row = output_row.strip() + '\n'
        self.f.write(output_row.encode('utf-8'))
        self.f.flush()


def is_file_io() -> bool:
    if _get_stripped_env_string(OUTPUT_DATA_JSON_FILE_PATH):
        return True
    else:
        return False


# Start: Grab stderr to log file.
class StdLogger(object):
    def __init__(self, level):
        self._msg = ''
        self.level = level

    def write(self, message):
        self._msg = self._msg + message
        while '\n' in self._msg:
            pos = self._msg.find('\n')
            self.level(self._msg[:pos])
            self._msg = self._msg[pos + 1:]

    def flush(self):
        if self._msg != '':
            self.level(self._msg)
            self._msg = ''


if is_file_io():
    file_writer = JsonFileIO()
    # Overriding stderr to logger.error
    sys.stderr = StdLogger(file_writer.write_stderr)

    # Overriding stdout to logger.info
    sys.stdout = StdLogger(file_writer.write_stdout)
