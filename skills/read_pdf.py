#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Read PDF file and extract text
"""

import fitz

def read_pdf(filename):
    """Read PDF file and extract text"""
    doc = fitz.open(filename)
    text = []
    for page in doc:
        text.append(page.get_text())
    return '\n'.join(text)

if __name__ == '__main__':
    filename = '/root/.openclaw/media/inbound/华宝通产品图册2020版---26054109-de29-4249-bbfd-d881bcc98ff6.pdf'
    text = read_pdf(filename)
    with open('/tmp/华宝通产品图册2020版.txt', 'w', encoding='utf-8') as f:
        f.write(text)
