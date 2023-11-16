import datetime

from pydantic import BaseModel


class TokenAntsToEditorBase(BaseModel):
    """
    Base schema for token_ants_to_editor table.
    """

    id_editor: int
    token: str
    validity_date: datetime


class TokenAntsToEditorCreate(TokenAntsToEditorBase):
    """
    Schema for creating a new token_ants_to_editor record.
    """

    pass


class TokenAntsToEditorUpdate(TokenAntsToEditorBase):
    """
    Schema for updating an existing token_ants_to_editor record.
    """

    pass


class TokenAntsToEditor(TokenAntsToEditorBase):
    """
    Schema for token_ants_to_editor table.
    """

    id: int

    class Config:
        orm_mode = True
