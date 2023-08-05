import re
import cv2
import numpy as np
import pytesseract
from PIL import Image, ImageFilter

from .textdetection import TextDetector

"""
This file will contain all code required to perform OCR.

"""


class OCR:

    def __init__(self):
        self.valid_text_expression = r'[1-9]\d*\s*(μ|u|n)m'

    def perform_ocr(self, image: np.ndarray, lang: str='eng', custom_config: str=None) -> str:
        custom_config = '--psm 6 -c tessedit_char_whitelist=0123456789\sunm'
        image = self.preprocess_image(image)
        text = pytesseract.image_to_string(image, lang=lang, config=custom_config)
        match = re.search(self.valid_text_expression, text)
        if match:
            text = match[0]
        else:
            text = None
        return text

    def get_text_from_rois(self, rois: list):
        valid_match = False
        text = None
        valid_idx = 0
        for i, roi in enumerate(rois):
            text = self.perform_ocr(roi)
            if text is not None:
                valid_match = True
                valid_idx = i
            if valid_match:
                break
        return text, valid_idx

    def preprocess_image(self, image):
        h, w = image.shape[:2]
        image = Image.fromarray(image)
        # increase resolution
        image = image.resize((int(w*2.5), int(h*2.5)), resample=Image.BICUBIC)
        # resize image for text detection (must be multiple of 32)
        h, w = np.array(image).shape[:2]
        new_h = int(h - (h % 32))
        new_w = int(w - (w % 32))
        image = image.resize((new_w, new_h), resample=Image.BICUBIC)
        image = np.array(image)
        return image
