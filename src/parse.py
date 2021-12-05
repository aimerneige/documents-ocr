#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: AimerNeige
# Date: 2021-12-04
# Mail: aimer.neige@aimerneige.com
# Github: aimerneige
# Version: 1.0
# License: MIT


import os
import csv
import json

threshold = 0.95
header = ["words", "average", "min", "variance", "result"]

def parse_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)


def create_csv(file_path):
    with open(file_path, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(header)


def write_csv(file_path, data_lines):
    with open(file_path, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data_lines)


def main():
    json_path = os.getcwd() + '/result'
    for file_name in os.listdir(json_path):
        file_path = os.path.join(json_path, file_name)
        obj = parse_json(file_path)
        words_result_list = obj['words_result']
        csv_name = os.path.basename(file_path) + '.csv'
        csv_path = os.path.join(os.getcwd(), 'csv/', csv_name)
        create_csv(csv_path)
        for words_result in words_result_list:
            probability = words_result['probability']
            average = probability['average']
            min = probability['min']
            variance = probability['variance']
            words = words_result['words']
            result = ''
            if average > threshold:
                result = words
            data_line = [words, average, min, variance, result]
            write_csv(csv_path, data_line)


if __name__ == '__main__':
    main()
