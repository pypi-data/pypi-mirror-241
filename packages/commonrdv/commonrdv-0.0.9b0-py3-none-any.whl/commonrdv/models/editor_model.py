from typing import Optional

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from ..db.postgresdb import Base
from .editor_model import Editor as EditorDTO

from .token_ants_to_editor import TokenAntsToEditor  # noqa: F401
from .token_editor_to_ants import TokenEditorToAnts  # noqa: F401


class Editor(Base):
    """
    A class representing the editor table in the database.

    Attributes:
    -----------
    id : int
        The primary key of the editor table.
    name : str
        The name of the editor.
    url : str
        The URL of the editor.
    header_name : str
        The header name of the editor.
    tokens_ants_to_editor : list
        A list of tokens from ants to editor.
    tokens_editor_to_ants : list
        A list of tokens from editor to ants.
    """

    __tablename__ = "editor"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    url = Column(String, nullable=False)
    header_name = Column(String, nullable=False)
    tokens_ants_to_editor = relationship("TokenAntsToEditor", back_populates="editor")
    tokens_editor_to_ants = relationship("TokenEditorToAnts", back_populates="editor")

    def clean_token(self):
            """
            Removes invalid tokens from the lists of tokens.
            """
            self.tokens_ants_to_editor = [
                token for token in self.tokens_ants_to_editor if token.is_valid()
            ]
            self.tokens_editor_to_ants = [
                token for token in self.tokens_editor_to_ants if token.is_valid()
            ]
    
    def to_dto(self):
        from .editor import Editor as DTO # noqa: F401
        self.clean_token()
        return DTO(
            url=self.url,
            name=self.name,
            test_mode=False,
            header_name=self.header_name,
            tokens_editor_to_ants=self.tokens_editor_to_ants,
            tokens_ants_to_editor=self.tokens_ants_to_editor,
            status=False,
        )