#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: AimerNeige
# Date: 2021-12-04
# Mail: aimer.neige@aimerneige.com
# Github: aimerneige
# Version: 1.0
# License: MIT


import sys
from pdf2image import convert_from_path

if __name__ == '__main__':
    args = sys.argv
    if len(args) < 2:
        print("Usage: python3 convert.py [pdf file path] [start index]")
        print("Note: you can ignore start index which will be 1 on default")
        exit()

    pdf_path = args[1]

    start_index = 1
    if len(args) == 3:
        start_index = int(args[2])

    images = convert_from_path(pdf_path)
    print('pdf converted to images')

    index = start_index
    for image in images:
        file_name = 'page_' + str(index).zfill(3) + '.png'
        file_path = './images/' + file_name
        image.save(file_path, 'png')
        print(file_path, ' saved')
        index += 1
