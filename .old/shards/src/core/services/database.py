#   SQLAlchemy imports
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.models.notes import Base

#   models
from core.models.notes import Note

#   Other imports
import yaml
import re
import logging

# Module-level logger
logger = logging.getLogger("database");


class DatabaseService:
    def __init__(self, db_url='sqlite:///obsidian.db', config_path='config.yaml'):
        """
        Initializes the database service.

        Args:
            db_url (str): The database URL.
            config_path (str): The path to the configuration file.
        """        
        try:
            self.engine = create_engine(db_url);
        except Exception as e:
            logger.error(f"[DatabaseService.__init__()] Error creating engine: {e}");
            return None;
        
        logger.info(f"[DatabaseService.__init__()] Engine created");
        
        try:
            self.Session = sessionmaker(bind=self.engine);
            Base.metadata.create_all(self.engine);
        except Exception as e:
            logger.error(f"[DatabaseService.__init__()] Error creating session: {e}");
            return None;
        
        logger.info(f"[DatabaseService.__init__()] Session created");
    
    def get_session(self):
        """
            Tries to access the database session.
        """
        try:
            session = self.Session();
        except Exception as e:
            logger.error(f"[DatabaseService.get_session()] Error accessing session: {e}");
            return None;        
        logger.info(f"[DatabaseService.get_session()] Session accessed");
        return session;
    
    
    def add_note(self, note_data: dict | Note) -> Note | None:
        """
        Adds a new note to the database.

        Args:
            note_data (dict | Note): The data for the new note, or a Note object.

        Returns:
            Note | None: The added note if successful, None otherwise.
        """
        # Access the session
        try:
            session = self.get_session();
        except Exception as e:
            logger.error(f"[DatabaseService.add_note()] < [self.get_session()] Error accessing session: {e}");
            return None;
        logger.info(f"[DatabaseService.add_note()] < [self.get_session()] Session accessed");
        
        # Create the note
        if isinstance(note_data, dict):
            try:
                note = Note(**note_data);
            except Exception as e:
                logger.error(f"[DatabaseService.add_note()] < [Note(**note_data)] Error creating note: {e}");
                return None;
            logger.info(f"[DatabaseService.add_note()] < [Note(**note_data)] Note created");
        elif isinstance(note_data, Note):
            note = note_data;
        else:
            logger.error(f"[DatabaseService.add_note()] Invalid `note_data` type: {type(note_data)} --- expected `dict` or `Note`");
            return None;
        
        # Add the note
        try:
            session.add(note);
        except Exception as e:
            logger.error(f"[DatabaseService.add_note()] < [session.add(note)] Error adding note: {e}");
            return None;
        logger.info(f"[DatabaseService.add_note()] < [session.add(note)] Note added");
        
        # Commit the changes
        logger.info(f"[DatabaseService.add_note()] < [session.commit()] Committing note");
        
        try:
            session.commit();
        except Exception as e:
            logger.error(f"[DatabaseService.add_note()] < [session.commit()] Error committing note: {e}");
            return None;
        logger.info(f"[DatabaseService.add_note()] < [session.commit()] Note committed");
        return note;