#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate a Word document for ZNS-09B1
"""

import sys
sys.path.insert(0, '/root/.openclaw/workspace/skills')

from generate_word_manual import generate_word_manual

with open('/root/.openclaw/workspace/华宝通智能门锁锂电池说明书_ZNS-09B1.md', 'r', encoding='utf-8') as f:
    content = f.read()

doc = generate_word_manual('华宝通智能门锁锂电池说明书（ZNS-09B1）', content)
doc.save('/root/.openclaw/workspace/华宝通智能门锁锂电池说明书_ZNS-09B1.docx')

print("Word document generated successfully!")
