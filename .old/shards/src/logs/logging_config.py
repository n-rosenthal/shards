"""
    Configuration for multi-module logging
"""

import logging
import sys
from pathlib import Path

def setup_logging(log_dir="logs", log_level=logging.INFO):
    """Configure root logger for the entire application"""
    log_dir = Path(log_dir)
    log_dir.mkdir(exist_ok=True)
    
    # Main formatter
    formatter = logging.Formatter(
        '[%(levelname)s] [%(asctime)s] [%(module)s:%(lineno)d] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Root logger configuration
    root_logger = logging.getLogger()
    root_logger.setLevel(log_level)
    
    # Clear existing handlers
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)
    
    # File handler (all modules)
    file_handler = logging.FileHandler(log_dir / 'shards.log')
    file_handler.setFormatter(formatter)
    root_logger.addHandler(file_handler)
    
    # Console handler (only for WARNING+)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.WARNING)
    console_formatter = logging.Formatter('%(levelname)s - %(message)s')
    console_handler.setFormatter(console_formatter)
    root_logger.addHandler(console_handler)
    
    # Module-specific log files
    module_loggers = {
        "database": logging.DEBUG,
        "parser": logging.INFO,
        "vault": logging.DEBUG
    }
    
    for module, level in module_loggers.items():
        logger = logging.getLogger(module)
        logger.setLevel(level)
        
        handler = logging.FileHandler(log_dir / f'{module}.log')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    
    return root_logger