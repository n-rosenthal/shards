from core.models.document import Document, Link
from core.models.models import Base, Column, String, JSON, Integer
from core.models.docid import docid as get_id


class Note(Base):
    __tablename__ = 'note'
    
    doc_id      = Column(String, primary_key=True)
    doctype     = Column(String(50), default='document')
    name        = Column(String(255), nullable=False)
    filepath    = Column(String(512), unique=True, nullable=False)
    tags        = Column(JSON, default=[])
    content     = Column(JSON, default={})
    
    """
        A `Note` is a document composed of a `yaml_header` and a `body` in Markdown format, both are fields of the `content` dictionary parameter.
    """
    def __init__(self, name: str = '', filepath: str = '', tags: list = [], content: dict = {}, *args, **kwargs):
        self.doc_id     = get_id();
        self.doctype    = "note" if not kwargs.get('doctype') else kwargs.get('doctype');
        self.name       = name;
        self.filepath   = filepath;
        self.tags       = tags;
        self.content    = content;
        
        if not isinstance(self.content, dict) or 'yaml_header' not in self.content or 'body' not in self.content:
            raise ValueError('The `content` parameter must be a dictionary with `yaml_header` and `body` keys.');
        
    @staticmethod
    def create(name: str, filepath: str, tags: list = [], content: dict = {}):
        return Note(name=name, filepath=filepath, tags=tags, content=content);
    
    
        
if __name__ == "__main__":
    note = Note.create(name='note', filepath='note.md', tags=['tempnote'], content={'body': 'This is a note.', 'yaml_header': {'doctype': 'note', 'date': '2023-01-01', 'title': 'Note', 'tags': ['tempnote']}});
    print(note.content);