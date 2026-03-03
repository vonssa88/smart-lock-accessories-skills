#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extract text from PDF file using OCR
"""

import fitz
import pytesseract
from PIL import Image
import io

def extract_text_from_pdf(filename):
    """Extract text from PDF file using OCR"""
    doc = fitz.open(filename)
    text = []
    for page in doc:
        # Convert page to image
        pix = page.get_pixmap()
        img = Image.open(io.BytesIO(pix.tobytes("png")))
        # OCR the image
        text.append(pytesseract.image_to_string(img, lang="chi_sim"))
    return '\n'.join(text)

if __name__ == '__main__':
    filename = '/root/.openclaw/media/inbound/华宝通产品图册2020版---26054109-de29-4249-bbfd-d881bcc98ff6.pdf'
    text = extract_text_from_pdf(filename)
    with open('/tmp/华宝通产品图册2020版.txt', 'w', encoding='utf-8') as f:
        f.write(text)
