#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: AimerNeige
# Date: 2021-12-04
# Mail: aimer.neige@aimerneige.com
# Github: aimerneige
# Version: 1.0
# License: MIT

import base64
import requests
from enum import Enum


TOKEN_URL = 'https://aip.baidubce.com/oauth/2.0/token'
OCR_URL = 'https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic'


class Language(Enum):
    auto_detect = 0
    CHN_ENG = 1
    ENG = 2
    JAP = 3
    KOR = 4
    FRE = 5
    SPA = 6
    POR = 7
    GER = 8
    ITA = 9
    RUS = 10
    DAN = 11
    DUT = 12
    MAL = 13
    SWE = 14
    IND = 15
    POL = 16
    ROM = 17
    TUR = 18
    GRE = 19
    HUN = 20


class OCR(object):

    def __init__(self, api_key, secret_key):
        super().__init__()
        self.API_KEY = api_key
        self.SECRET_KEY = secret_key
        self.ACCESS_TOKEN = self.fetch_token()
        self.LANGUAGE = Language.auto_detect.name
        self.DETECT_DIRECTION = "false"
        self.PARAGRAPH = "false"
        self.PROBABILITY = "true"

    def set_language(self, language):
        self.LANGUAGE = language.name

    def set_detect_direction(self, detect_direction):
        self.DETECT_DIRECTION = detect_direction

    def set_paragraph(self, paragraph):
        self.PARAGRAPH = paragraph

    def set_probability(self, probability):
        self.PROBABILITY = probability

    def fetch_token(self):
        response = requests.post(TOKEN_URL, data={
            'grant_type': 'client_credentials',
            'client_id': self.API_KEY,
            'client_secret': self.SECRET_KEY
        })
        if response:
            return response.json()['access_token']

    def encode_image(self, image_path):
        with open(image_path, 'rb') as f:
            image_data = f.read()
        return base64.b64encode(image_data)

    def encode_pdf(self, pdf_path):
        with open(pdf_path, 'rb') as f:
            pdf_data = f.read()
        return base64.b64encode(pdf_data)

    def get_ocr_result_image(self, image_path):
        request_url = OCR_URL + '?access_token=' + self.ACCESS_TOKEN
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        params = {
            'image': self.encode_image(image_path),
            'language_type': self.LANGUAGE,
            'detect_direction': self.DETECT_DIRECTION,
            'paragraph': self.PARAGRAPH,
            'probability': self.PROBABILITY,
        }
        response = requests.post(request_url, headers=headers, data=params)
        return response.json()

    def get_ocr_result_pdf(self, pdf_path, page_num=0):
        request_url = OCR_URL + '?access_token=' + self.ACCESS_TOKEN
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        params = {
            'pdf_file': self.encode_pdf(pdf_path),
            'pdf_file_num': page_num,
            'language_type': self.LANGUAGE,
            'detect_direction': self.DETECT_DIRECTION,
            'paragraph': self.PARAGRAPH,
            'probability': self.PROBABILITY,
        }
        response = requests.post(request_url, headers=headers, data=params)
        return response.json()
