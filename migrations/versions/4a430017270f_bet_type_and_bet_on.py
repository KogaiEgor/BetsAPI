"""Bet type and Bet on

Revision ID: 4a430017270f
Revises: 193415b3b0c3
Create Date: 2024-02-28 15:52:00.352655

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4a430017270f'
down_revision: Union[str, None] = '193415b3b0c3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
