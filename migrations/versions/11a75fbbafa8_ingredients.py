"""ingredients

Revision ID: 11a75fbbafa8
Revises: 449aea8d4eb5
Create Date: 2026-06-15 11:07:42.156246

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '11a75fbbafa8'
down_revision: Union[str, None] = '449aea8d4eb5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
            CREATE TABLE ingredients (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL UNIQUE,
            created_at TIMESTAMP NOT NULL,
            );
        """
    )


def downgrade() -> None:
    op.execute(
        """
            DROP TABLE ingredients
        """
    )
