import csv
import sys
import datetime
from re import sub
from gitlab_evaluate.lib import limits


def write_to_csv(file_path, headers, data, append=False):
    '''
        Writes dictionary data to CSV file

        :param file_path: (str) path to where the CSV will be created
        :param headers: (list[str]) list of strings containing the headers for the CSV
        :param data: (dict) the data to be written to the CSV
        :param append: (bool) If set to True, headers will not be written and an existing file will get appended
    '''
    try:
        file_action = 'w' if not append else 'a'
        with open(file_path, file_action) as cf:
            writer = csv.DictWriter(cf, fieldnames=headers)
            if not append:
                writer.writeheader()
            for entry in data:
                writer.writerow(entry)
    except IOError:
        print(f"\nI/O error. Cannot create {file_path}")
        print(f"Ensure you have the proper permissions to create {file_path}.\n")
        sys.exit()

def write_headers(row_index, worksheet, headers, cell_format):
    for i in range(0, len(headers)):
        worksheet.write(row_index, i, headers[i], cell_format)

def write_to_workbook(worksheet, data, headers):
    for row, r in enumerate(data, start=1):
        for col, h in enumerate(headers):
            worksheet.write(row, col, r.get(h, ''))

def append_to_workbook(worksheet, data, headers):
    row = len(worksheet.table)
    for d in data:
        for col, h in enumerate(headers):
            write_to_worksheet(worksheet, row, col, d.get(h, ''))

def write_to_worksheet(worksheet, row, col, item):
    if isinstance(item, bool):
        worksheet.write(row, col, str(item))
    elif isinstance(item, str):
        worksheet.write(row, col, item)
    elif isinstance(item, (int, float)):
        worksheet.write_number(row, col, item)

def check_size(k, v):
    # TODO: Dictionary of function pointers
    if k == "storage_size":
        return check_storage_size(v)
    if k == "commit_count":
        return check_num_commits(v)
    if k == "repository_size":
        return check_file_size(v)

def check_num_pl(i):
    return i > limits.PIPELINES_COUNT

def check_num_br(i):
    return i > limits.BRANCHES_COUNT

def check_num_commits(i):
    return i > limits.COMMITS_COUNT

def check_storage_size(i):
    '''Includes artifacts, repositories, wiki, and other items.'''
    return i > limits.STORAGE_SIZE

def check_registry_size(i):
    return i > limits.CONTAINERS_SIZE

### File size limit is 5GB
def check_file_size(i):
    return i > limits.FILE_SIZE

def check_num_issues(i):
    return i > limits.ISSUES_COUNT

def check_num_mr(i):
    return i > limits.MERGE_REQUESTS_COUNT

def check_num_tags(i):
    return i > limits.TAGS_COUNT

def check_proj_type(i):
    return i

def sizeof_fmt(num, suffix="B"):
    for unit in ["", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"]:
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Yi{suffix}"

def to_camel_case(s):
    """
        Shameless copy from https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-96.php
    """
    s = sub(r"(_|-)+", " ", s).title().replace(" ", "")
    return ''.join([s[0].lower(), s[1:]])

def get_date_run():
    return datetime.datetime.now().date().strftime("%Y-%m-%d")

def get_countif(sheet_name, search_string, column_letter):
    return f'COUNTIF(\'{sheet_name}\'!{column_letter}:{column_letter}, "{search_string}")'

def get_countifs(sheet_name, search_string_1, column_letter_1, search_string_2, column_letter_2):
    return f'COUNTIFS(\'{sheet_name}\'!{column_letter_1}:{column_letter_1}, "{search_string_1}", \'{sheet_name}\'!{column_letter_2}:{column_letter_2}, "{search_string_2}")'

def get_counta(sheet_name, column_letter):
    return f'COUNTA(\'{sheet_name}\'!{column_letter}:{column_letter})'

def get_if(logical_expression, value_if_true, value_if_false):
    return f'IF({logical_expression}, {value_if_true}, {value_if_false})'

def get_sum(sheet_name, column_letter):
    return f'SUM(\'{sheet_name}\'!{column_letter}:{column_letter})'

def get_sumif(sheet_name, column_letter_1, column_letter_2, search_string):
    return f'SUMIF(\'{sheet_name}\'!{column_letter_1}:{column_letter_1}, "{search_string}", \'{sheet_name}\'!{column_letter_2}:{column_letter_2})'

def get_reading_the_output_link():
    return 'https://gitlab.com/gitlab-org/professional-services-automation/tools/utilities/evaluate/-/blob/main/reading-the-output.md?ref_type=heads'

def get_upgrade_path(gitlab_version):
    return 'https://gitlab-com.gitlab.io/support/toolbox/upgrade-path/?current='+gitlab_version
