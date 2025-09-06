"""
    `core/services/writers/yaml_writer.py`
    
    YAML writer. Standard function for writing YAML headers to documents.
"""

import yaml;

def yaml_to_str(yaml_header: dict) -> str:
    """
        Converts a dictionary to a YAML string.
    """
    return yaml.dump(yaml_header);
    