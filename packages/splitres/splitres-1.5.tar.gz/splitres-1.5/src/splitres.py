"""Realization splitres.sh on python"""
import re
import os
import argparse
from statistics import mean
from typing import Dict, List
import sys


def splitres(file_path, result_dir):
    """
    Function calculates the min, max, average and sum of
    power consumption value and writes this data to a file.

    Args:
        file_path (str): path to the file or directory with files with the messtat-extension.
        result_dir (str): path to the directory in which will be written files.

    Returns:
        return_val (list): list of result which will be written to a file.(need it for testing)
    """
    file_path = str(file_path)
    result_dir = str(result_dir)

    if os.path.isdir(file_path):
        return_val = []
        for root, _pre_dir, files in os.walk(file_path):
            for file in files:
                if file.endswith('.messtat'):
                    path = os.path.join(root, file)
                    err, val = splitres_for_file(path, result_dir)
                    if err == -1:
                        print(val, file=sys.stderr)
                        continue

                    return_val.append(val)
    elif file_path.endswith('.messtat'):
        err, return_val = splitres_for_file(file_path, result_dir)
        if err == -1:
            print(return_val, file=sys.stderr)
            return_val = None
        else:
            return_val = [return_val]

    else:
        print("File isn\'t exist!", file=sys.stderr)
        return_val = None
    return return_val


def splitres_for_file(file_path, result_dir):
    """
    This function is a helper for function for splitres.
    It's works directly with files with the messtat-extension

    Args:
        file_path (str): path to the file with the messtat-extension.
        result_dir (str): path to the directory in which will be written result-files.

    Returns:
        err (int): indicator of errors. If errors was, returns value is -1, else it's will be 0.
        results_list (list): list of result which will be written to a file.(need it for testing)
    """
    err, data = parser_for_messtatfile(file_path)
    if err == -1:
        return err, data

    _, results_dict = counting_values(data)

    file_name = os.path.split(file_path)[1]
    new_file_path = os.path.join(result_dir, file_name)

    err, text_error = write_to_file(new_file_path, results_dict)
    if err == -1:
        return err, text_error

    return err, results_dict


def parser_for_messtatfile(file_name):
    """
    This function parse messtat files and cut from them
    necessary information(info about power consumption in J).

    Args:
        file_name (str): path to the file or directory with files with the messtat-extension.

    Returns:
        err (int): indicator of errors. If errors was, returns value is -1, else it's will be 0.
        data (list): list of values which parsed from messtat file.
    """

    data = list()
    err = 0

    try:
        with open(file_name, 'r') as file:
            for line in file.read().split('\n'):
                if 'package' in line:
                    num = float(re.findall(r'\d+[,.]\d+', line.split(' ')[1])[0].replace(",", "."))
                    data.append(num)
    except PermissionError as ex:
        data = str(ex)
        err = -1
    except FileNotFoundError as ex:
        data = str(ex)
        err = -1

    return err, data


def counting_values(data: List[float]):
    """
    Function that count min, max, average and sum of elements in data list.

    Args:
        data (list): list of values which parsed from messtat file.

    Returns:
        err (int): indicator of errors. If errors was, returns value is -1, else it's will be 0.
        results_dict (dict): dictionary which contain min, max, average and sum of data elements.
    """
    results_dict = dict()
    err = 0
    try:
        results_dict = {
            'Min': min(data),
            'Max': max(data),
            'Mean': mean(data),
            'Sum': sum(data),
        }
    except TypeError as ex:
        results_dict = str(ex)
        err = -1
    except ValueError as ex:
        results_dict = {}
        err = 0

    return err, results_dict


def write_to_file(path, results: Dict[str, float]):
    """
    Function that do writing information about power consumption and
    name of a file, which was parsed, to a file.

    Args:
        path (str): path to the file or directory with files with the messtat-extension.
        results (dict): dict which contain min, max, average and sum of data elements.

    Returns:
        err (int): indicator of errors. If errors was, returns value is -1, else it's will be 0.
        text_error (str): this value contain text of error which will print if error was.
    """
    if not isinstance(results, dict):
        return -1, 'Incorrect type results'

    if not isinstance(path, str):
        return -1, 'Incorrect type path'

    file_name = os.path.split(path)[1]
    dir_name = os.path.split(path)[0]
    new_file_name = 'messtat_%s.spliter' % file_name
    out_file_name = os.path.join(dir_name, new_file_name)

    text = str()
    for key in results:
        text += '%s: %s\n' % (key, results[key])

    text_error = str()
    err = 0
    try:
        with open(out_file_name, "a+") as file:
            file.write(text)
    except PermissionError as ex:
        text_error = str(ex)
        err = -1
    except FileNotFoundError as ex:
        text_error = str(ex)
        err = -1

    return err, text_error


def check_exist_dir(dir_name):
    """
    This function check result-directory, if it's doesn't exist function create that directory.

    Args:
        dir_name (str): name of directory in which we want write our files.

    Returns:
        err (int): indicator of errors. If errors was, returns value is -1, else it's will be 0.
        text_error (str): this value contain text of error which will print if error was.
    """
    if not isinstance(dir_name, str):
        return -1, 'Your enter incorrect value'

    err = 0
    text_error = str()
    if os.path.exists(dir_name) != 1:
        try:
            os.mkdir(dir_name)
        except PermissionError as ex:
            err = -1
            text_error = str(ex)
        except FileExistsError as ex:
            err = -1
            text_error = str(ex)
        except FileNotFoundError as ex:
            err = -1
            text_error = str(ex)
    return err, text_error

def main():
    """
    Main function that works with arguments of command line.

    Args:

    Returns:
        None
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(dest='file_path',
                        help='Specifies the path to a file or directory '
                             'containing files with the required extension')
    parser.add_argument(dest='result_path', nargs='?', default='result',
                        help='Specifies the path to directory in which would '
                             'writting the spliter-files. By default it will be "result"')
    args = parser.parse_args()

    if args.file_path:
        path_name = os.path.abspath(args.file_path)
        dir_name = str(args.result_path)
        err, text_error = check_exist_dir(dir_name)
        if err == -1:
            print(text_error, file=sys.stderr)
            return

        splitres(path_name, dir_name)


if __name__ == '__main__':
    main()
