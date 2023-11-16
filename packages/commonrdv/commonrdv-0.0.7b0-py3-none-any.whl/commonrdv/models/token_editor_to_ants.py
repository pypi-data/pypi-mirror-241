from datetime import datetime


from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..db.postgresdb import Base




class TokenEditorToAnts(Base):
    """
    Represents a token assigned to an editor for accessing the ANTS API.
    """

    __tablename__ = "token_editor_to_ants"

    id = Column(Integer, primary_key=True, index=True)
    id_editor = Column(Integer, ForeignKey("editor.id"))
    token = Column(String, unique=True, nullable=False)
    validity_date = Column(DateTime, nullable=False)
    editor = relationship("Editor", back_populates="tokens_editor_to_ants")

    def is_valid(self):
        """
        Returns True if the token is valid (i.e., the validity date is in the future or not set), False otherwise.
        """
        return self.validity_date is None or self.validity_date > datetime.now()
