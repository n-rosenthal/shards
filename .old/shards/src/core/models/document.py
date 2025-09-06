""" `models/document.py`
    The `Document` model is the base class for other documents (texts, notes, entries &c) objects stored in the database.
"""


from sqlalchemy                 import  Column, Integer, String, DateTime, JSON
from sqlalchemy.ext.declarative import  declarative_base
from core.models.models                     import  Base
from core.models.docid                      import  docid as get_id
import datetime;

class Document(Base):
    """
        Base class for other text-based, Markdown documents.
    """
    __tablename__ = "document"
    
    doc_id      = Column(String, primary_key=True)
    doctype     = Column(String(50), default='document')
    name        = Column(String(255), nullable=False)
    filepath    = Column(String(512), unique=True, nullable=False)
    tags        = Column(JSON, default=[])
    content     = Column(JSON, default={})
    
    def __init__(self, doctype: str = 'document', name: str = '', filepath: str = '', tags: list = [], content: dict = {}):
        self.doc_id     = get_id();
        self.doctype    = doctype;
        self.name       = name;
        self.filepath   = filepath;
        self.tags       = tags;
        self.content    = content;
        
    @staticmethod
    def create(name: str, filepath: str, tags: list = [], content: dict = {}):
        return Document(name=name, filepath=filepath, tags=tags);
    
    def __repr__(self):
        return f"Document(doc_id={self.doc_id}, doctype={self.doctype}, name={self.name}, filepath={self.filepath}, tags={self.tags}, content={self.content})";
    
    def __str__(self):
        return f"Document(doc_id={self.doc_id}, doctype={self.doctype}, name={self.name}, filepath={self.filepath}, tags={self.tags}, content={self.content})";
    
class Link(Base):
    """
        Stablish a link between two documents.
    """
    __tablename__ = "link"
    
    doc_from    = Column(String, primary_key=True)
    doc_to      = Column(String, primary_key=True)
    created_at  = Column(DateTime, default=datetime.datetime.now())
    
    def __init__(self, doc_from: str, doc_to: str):
        self.doc_from = doc_from;
        self.doc_to   = doc_to;
        self.created_at = datetime.datetime.now();
        
    def __repr__(self):
        return f"Link(doc_from={self.doc_from}, doc_to={self.doc_to}, created_at={self.created_at})";
    
    def __str__(self):
        return f"Link(doc_from={self.doc_from}, doc_to={self.doc_to}, created_at={self.created_at})";
    
    @staticmethod
    def create(doc_from: str, doc_to: str):
        return Link(doc_from=doc_from, doc_to=doc_to);
    
class DocumentGraph(Base):
    __tablename__ = "document_graph"
    
    graph_id: int = Column(Integer, primary_key=True, autoincrement=True);
    documents: list[Document] = Column(JSON);
    links: list[Link] = Column(JSON);
    
    
    """
        A `DocumentGraph` is a relation of `Document` objects and `Link` objects that connect them. It is, therefore, a graph of `Document` vertices and `Link` edges.
    """
    def __init__(self, documents: list[Document], links: list[Link]):
        self.documents = documents;
        self.links = links;
        
    def __repr__(self):
        return f"DocumentGraph(documents={self.documents}, links={self.links})";
    
    def __str__(self):
        return f"DocumentGraph(documents={self.documents}, links={self.links})";
    

#   ============================================================================
#   Special `Document` objects
#   ============================================================================
ROOT_DOCUMENT : Document = Document.create(name="Root Document", filepath="/", tags=["root"]);

#   ============================================================================
#   Special `Link` objects
#   ============================================================================
def to_root(doc: Document) -> Link:
    """
        Connects the given document to the `ROOT_DOCUMENT` in the database.
    """
    return Link.create(doc_from=doc.doc_id, doc_to=ROOT_DOCUMENT.doc_id);