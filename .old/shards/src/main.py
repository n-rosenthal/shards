"""
    main
"""

#   Logging initialization for multi-module logging
import logging
from logs.logging_config import setup_logging
logger : logging.Logger = setup_logging(log_dir="logs", log_level=logging.DEBUG);

#   Services
##   Database
from core.services.database import DatabaseService

##  Vault Management
from core.services.vault import VaultManager


if __name__ == "__main__":
    #   Initialize the database
    logger.info("Initializing database. . . ");
    db : DatabaseService = DatabaseService(db_url='sqlite:///obsidian.db', config_path='config.yaml');
    if db is None:
        logger.error("Database initialization failed");
        exit(1);
    else:
        logger.info("Database initialized.");
    
    #   Initialize the vault manager
    logger.info("Initializing vault manager . . .");
    vault : VaultManager = VaultManager(vault_path='./vaults/b/b');
    
    if vault is None:
        logger.error("Vault manager initialization failed");
        exit(1);
    else:
        logger.info("Vault manager initialized.");