#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: AimerNeige
# Date: 2021-12-04
# Mail: aimer.neige@aimerneige.com
# Github: aimerneige
# Version: 1.0
# License: MIT

import os
import json
from key import *
from ocr import *

if __name__ == '__main__':
    ocr = OCR(API_KEY, SECRET_KEY)
    ocr.set_detect_direction("false")
    ocr.set_language(Language.CHN_ENG)
    ocr.set_paragraph("false")
    ocr.set_probability("true")

    images_path = os.getcwd() + "/images"
    for filename in os.listdir(images_path):
        image_path = os.path.join(images_path, filename)
        print('start to recognize ', image_path)
        result = ocr.get_ocr_result_image(image_path)
        file_name = os.path.basename(image_path) + '.json'
        file_path = './result/' + file_name
        with open(file_path, 'w') as f:
            f.write(json.dumps(result, ensure_ascii=False))
        print(image_path, 'recognized successfully')
    print('all done')
