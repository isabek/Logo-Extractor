import argparse
import json
import os
import sys


def read_file_skip_header_lazy(file):
    with open(file, "r") as f:
        next(f)
        for line in f.readlines():
            yield line


def _read_actual_file(actual_file):
    actual_items = {}
    for line in read_file_skip_header_lazy(actual_file):
        url, logo_url = line.split(",")
        url, logo_url = url.strip().strip("/"), logo_url.strip().strip("/")
        if not actual_items.get(url):
            actual_items[url] = logo_url
    return actual_items


def _read_json_file(json_file):
    predicted_items = {}
    with open(json_file) as f:
        data = json.load(f)
        for line in data:
            url, logo_url = line['webpage_url'].strip().strip("/"), line['logo_url'].strip().strip("/")
            if not predicted_items.get(url):
                predicted_items[url] = logo_url
    return predicted_items


def compare(actual_file, json_file):
    actual_items = _read_actual_file(actual_file)
    predicted_items = _read_json_file(json_file)

    result = {
        'Equal': [],
        'Not Equal': [],
        'Not Found': [],
    }

    for url, logo_url in actual_items.items():
        predicted_logo_url = predicted_items.get(url)
        if predicted_logo_url == logo_url:
            result['Equal'].append(url)
        elif not predicted_logo_url:
            result['Not Found'].append(url)
        else:
            result['Not Equal'].append(url)

    for key, items in result.items():
        print("-" * 124)
        print("| {} | {} |\n".format(key, len(items)))
        for item in items:
            print("| {:<120} |".format(item))
        print("-" * 124)
        print()


def main():
    parser = argparse.ArgumentParser(description="Checker for actual vs scraped logo url")
    parser.add_argument("-actual", help="Location of actual txt file", required=True)
    parser.add_argument("-json", help="Location of JSON file", required=True)
    args = parser.parse_args()

    def file_abs_path(file_name):
        return os.path.join(os.path.dirname(os.path.realpath('__file__')), file_name)

    actual_file = file_abs_path(args.actual)
    if not os.path.isfile(actual_file):
        print("Provide the correct actual file.")
        sys.exit()

    json_file = file_abs_path(args.json)
    if not os.path.isfile(json_file):
        print("Provide the correct JSON file.")
        sys.exit()

    compare(actual_file, json_file)


if __name__ == '__main__':
    main()
