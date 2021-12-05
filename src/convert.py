#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: AimerNeige
# Date: 2021-12-04
# Mail: aimer.neige@aimerneige.com
# Github: aimerneige
# Version: 1.0
# License: MIT


from pdf2image import convert_from_path

if __name__ == '__main__':

    images = convert_from_path('example.pdf')
    print('pdf converted to images')

    index = 1
    for image in images:
        file_name = 'page_' + str(index).zfill(3) + '.png'
        file_path = './images/' + file_name
        image.save(file_path, 'png')
        print(file_path, ' saved')
        index += 1
