"""
    `ftparser.py`   Domain-specific parser for `fleeting-thoughts` notes.
    
    A `fleeting-thought` note has the format:
   
    ```markdown
    ---
    doctype: fleeting-thought
    title: <title>
    date: <date>
    tags:
      - fleeting-thought
    ---
    
    # (fleeting-thought) <title>
    ---
    
    <body>
    ---
    ```
    
    Therefore, it is possible to fully represent any `fleeting-thought` note by a tuple of the form `(title, date, [tags optional], body)`, which is implemented as a dictionary with keys `title`, `date`, `tags`, and `body`.
"""
import logging;
from core.services.parsers.yaml_parse import yaml_parse, yaml_parse, yaml_get
from src.core.services.parsers.yaml_parse import yaml_extract

logger: logging.Logger = logging.getLogger("ftparser");



#   Transactional type for the `fleeting-thought` category
FleetingThought = dict[str, str | list[str] | str];

def ft_parse(fleeting_thought_text: str) -> FleetingThought | None:
    """
        Tries to parse a `fleeting-thought` note.
    """
    try:
        yaml_header: dict = yaml_parse(yaml_extract(fleeting_thought_text));
        if yaml_header:
            doctype: str = yaml_header.get('doctype');
            if doctype == 'fleeting-thought':
                title: str = yaml_header.get('title');
                date: str = yaml_header.get('date');
                tags: list[str] = yaml_header.get('tags', []);
                body: str = yaml_header.get('body');
                return {'title': title, 'date': date, 'tags': tags, 'body': body};
            else:
                logger.warning("[ft_parse()] < [yaml_parse()]] YAML frontmatter does not contain `doctype: fleeting-thought`: `%.63s`...", fleeting_thought_text.replace('\n', ' '));
                return None;    
        else:
            logger.warning("[ft_parse()] < [yaml_parse()]] No YAML frontmatter found in text: `%.63s`...", fleeting_thought_text.replace('\n', ' '));
            return None;
    except Exception as e:
        logger.exception("[ft_parse()] < [yaml_parse()]] Unexpected error during parsing\n\t%s", e);
    return None;
    
