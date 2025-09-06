"""
    `core/services/writers/ftwriter.py`
    Writer for the `fleeting-thought` note type.
"""

from core.services.writers.yaml_writer import yaml_to_str

FLEETING_THOUGHT_FORMAT : str = """
---
doctype: fleeting-thought
title: <title>
date: <date>
tags:,
  - fleeting-thought
keywords:,
---

# (fleeting-thought) <title>
---
<body>

---
""";

def ft_write(title: str, date: str, body: str, tags: list[str] = [], keywords: list[str] = []) -> str:
    #   replaces the title and the date in the template
    fleeting_thought_note = FLEETING_THOUGHT_FORMAT.replace('<title>', title).replace('<date>', date);
    
    #   if there are tags, append them
    if len(tags) > 0:
        _tags: str = ',\n  - fleeting-thought' + '\n  - '.join(tags);
        fleeting_thought_note = fleeting_thought_note.replace(',\n  - fleeting-thought', _tags);
    
    #   if there are keywords, append them
    if len(keywords) > 0:
        _keywords: str = ',\n' + '\n  - '.join(keywords);
        fleeting_thought_note = fleeting_thought_note.replace(',\n  - fleeting-thought', _keywords);
    
    #   replaces the body in the template
    fleeting_thought_note = fleeting_thought_note.replace('<body>', body);
    
    return fleeting_thought_note;