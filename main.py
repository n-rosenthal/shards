import logging
from src.config.logging_config import setup_logging;
setup_logging();
logger = logging.getLogger(__name__);

from src.models.Document    import Document
from src.models.Text        import TextType

from src.services.database.DatabaseService import DatabaseService



def main() -> int:
    logger.debug("[main()] initializing database");
    #   initialise database
    db = DatabaseService("sqlite:///database.db", True);
    
    logger.debug("[main()] finished running");
    return 0;

if __name__ == '__main__':
    exit(main());