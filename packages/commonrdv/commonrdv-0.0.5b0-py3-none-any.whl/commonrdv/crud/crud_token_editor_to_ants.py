from typing import Optional

from sqlalchemy.orm import Session

from ..crud.base import CRUDBase
from ..models.token_editor_to_ants import TokenEditorToAnts
from ..schemas.token_editor_to_ants import (
    TokenEditorToAntsCreate, TokenEditorToAntsUpdate)


class CRUDTokenEditorToAnts(
    CRUDBase[TokenEditorToAnts, TokenEditorToAntsCreate, TokenEditorToAntsUpdate]
):
    """
    CRUD operations for TokenEditorToAnts model.
    """

    def get_by_token(self, db: Session, *, token: str) -> Optional[TokenEditorToAnts]:
        """
        Retrieve a token by its value.

        Args:
            db (Session): SQLAlchemy session object.
            token (str): Token value.

        Returns:
            Optional[TokenEditorToAnts]: TokenEditorToAnts object if found, else None.
        """
        return (
            db.query(TokenEditorToAnts).filter(TokenEditorToAnts.token == token).first()
        )

    def get_all(self, db: Session):
        """
        Retrieve all tokens.

        Args:
            db (Session): SQLAlchemy session object.

        Returns:
            List[TokenEditorToAnts]: List of all TokenEditorToAnts objects.
        """
        return db.query(TokenEditorToAnts).all()


tokenEditorToAnts = CRUDTokenEditorToAnts(TokenEditorToAnts)
