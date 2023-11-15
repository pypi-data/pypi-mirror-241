"""
This module contains Pydantic schemas for database models related to token and editor entities.
It includes the following schemas:
- TokenAntsToEditorBase
- TokenAntsToEditorCreate
- TokenAntsToEditor
- TokenEditorToAntsBase
- TokenEditorToAntsCreate
- TokenEditorToAnts
- EditorBase
- EditorCreate
- EditorUpdate
- Editor
"""
import datetime

from pydantic import BaseModel


class TokenAntsToEditorBase(BaseModel):
    """
    Base schema for token issued by ANTS to editor
    """

    id: int
    id_editor: int
    token: str
    validity_date: datetime

    class Config:
        orm_mode = True


class TokenAntsToEditorCreate(TokenAntsToEditorBase):
    """
    Schema for creating token issued by ANTS to editor
    """

    pass


class TokenAntsToEditor(TokenAntsToEditorBase):
    """
    Schema for token issued by ANTS to editor
    """

    pass


class TokenEditorToAntsBase(BaseModel):
    """
    Base schema for token issued by editor to ANTS
    """

    id: int
    id_editor: int
    token: str
    validity_date: datetime

    class Config:
        orm_mode = True


class TokenEditorToAntsCreate(TokenEditorToAntsBase):
    """
    Schema for creating token issued by editor to ANTS
    """

    pass


class TokenEditorToAnts(TokenEditorToAntsBase):
    """
    Schema for token issued by editor to ANTS
    """

    pass


class EditorBase(BaseModel):
    """
    Base schema for editor
    """

    name: str
    url: str
    header_name: str


class EditorCreate(EditorBase):
    """
    Schema for creating editor
    """

    pass


class EditorUpdate(EditorBase):
    """
    Schema for updating editor
    """

    pass


class Editor(EditorBase):
    """
    Schema for editor
    """

    id: int

    class Config:
        orm_mode = True
