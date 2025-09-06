import yaml
import re
import logging

# Module-level logger
logger = logging.getLogger("yaml_parse");

def yaml_extract(text: str) -> str | None:
    """
    Extract YAML frontmatter from the given text.

    If the given text contains YAML frontmatter in the form of a block
    starting with "---" and ending with "---", then this function
    returns that block. Otherwise, it returns None.

    :param text: The text to extract YAML frontmatter from
    :return: The extracted YAML frontmatter if found, else None
    """
    pattern = r'^\s*---\s*\n(.*?)\n\s*---\s*(\n|$)'
    yaml_match = re.search(pattern, text, re.DOTALL)
    
    if yaml_match:
        # Return the entire matched block including delimiters
        block = yaml_match.group(0)
        logger.info("[yaml_extract()] Found YAML frontmatter: `%.63s`...", block.replace('\n', ' '))
        return block
    else:
        logger.warning("[yaml_extract()] No YAML frontmatter found in text: `%.63s`...", text.replace('\n', ' '))
        return None

def yaml_parse(yaml_string: str) -> dict | None:
    try:
        #   Remove delimiters
        yaml_string = yaml_string.strip('---\n')
        
        # Load the first document from the YAML string
        yaml_dict = yaml.safe_load(yaml_string)
        
        if isinstance(yaml_dict, dict) and yaml_dict:
            logger.info("[yaml_parse()] < [yaml.safe_load()]] Successfully parsed YAML")
            return yaml_dict
        else:
            logger.warning("[yaml_parse()] < [yaml.safe_load()]] Parsed empty or invalid YAML structure")
            return None
            
    except yaml.YAMLError as e:
        logger.error("[yaml_parse()] < [yaml.safe_load()]] YAML parsing error: %s", e)
    except Exception as e:
        logger.exception("[yaml_parse()] < [yaml.safe_load()]] Unexpected error during parsing\n\t%s", e)
    return None

def yaml_to_str(yaml_str: str) -> str:
    try:
        #   Remove delimiters
        yaml_str = yaml_str.strip('---\n');
        
        return yaml.dump(yaml.safe_load(yaml_str));
    except yaml.YAMLError as e:
        logger.error("[yaml_to_str()] < [yaml.dump()]] YAML dumping error: %s", e)
    except Exception as e:
        logger.exception("[yaml_to_str()] < [yaml.dump()]] Unexpected error during dumping\n\t%s", e)
    return ""

def yaml_get(text: str) -> tuple[str | None, str | None]:
    try:
        #   frontmatter
        yaml_frontmatter: str | None = yaml_extract(text);
        if yaml_frontmatter:
            yaml_frontmatter = yaml_to_str(yaml_frontmatter);
        else:
            yaml_frontmatter = "";
        
        
        #   remainder: clear from --- to ---
        text = re.sub(r'^\s*---\s*\n(.*?)\n\s*---\s*(\n|$)', '', text, flags=re.DOTALL);
        text = text.strip();
        
        return (yaml_frontmatter, text);
    except Exception as e:
        logger.exception("[yaml_get()] < [yaml.dump()]] Unexpected error during dumping\n\t%s", e);
    return ("", text);


