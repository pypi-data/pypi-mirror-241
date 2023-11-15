from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..db.postgresdb import Base


class TokenAntsToEditor(Base):
    """
    Represents a token used to authenticate an editor in the ANTS system.
    """

    __tablename__ = "token_ants_to_editor"

    id = Column(Integer, primary_key=True, index=True)
    id_editor = Column(Integer, ForeignKey("editor.id"))
    token = Column(String, unique=True, nullable=False)
    validity_date = Column(DateTime, nullable=False)
    editor = relationship("Editor", back_populates="tokens_ants_to_editor")

    def is_valid(self):
        """
        Returns True if the token is still valid, False otherwise.
        """
        return self.validity_date is None or self.validity_date > datetime.now()
