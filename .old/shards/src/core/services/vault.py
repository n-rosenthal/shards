"""
    Obisidian Vault management service
"""

import logging;

logger = logging.getLogger("vault");


from pathlib import Path
from core.services.database import DatabaseService



class VaultManager:
    def __init__(self, vault_path: str):
        #   Check if vault path is valid
        if not Path(vault_path).is_dir():
            logger.error(f"[VaultManager.__init__()] Invalid vault path: {vault_path}");
            return None;
        logger.info(f"[VaultManager.__init__()] initialized VaultManager for path `{vault_path}`");
        
        self.vault_path = Path(vault_path);
        
        #   Initialize database
        self.db = DatabaseService();
    
        if self.db is None:
            logger.error("[VaultManager.__init__()] < [DatabaseService()] Database initialization failed");
            return None;
        else:
            logger.info("[VaultManager.__init__()] < [DatabaseService()] Database initialized for VaultManager");
            
        #   Scan vault
        self.scan_vault();
    
    
    def scan_vault(self) -> None:
        """Scan entire vault and update database"""
        counter: int = 0;
        
        for md_file in self.vault_path.glob('**/*.md'):
            if md_file.is_file():
                self.process_note(md_file)
                counter += 1;
                
                logger.debug(f"[VaultManager.scan_vault()] processed file: {counter}, \"{md_file}\"");
                
        logger.info(f"[VaultManager.scan_vault()] Processed {counter} files");
        
    
    def process_note(self, filepath: Path):
        """Process individual note file"""
        return;