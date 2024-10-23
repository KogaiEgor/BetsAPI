"""Bet type and Bet on

Revision ID: 193415b3b0c3
Revises: 7615afcfbec4
Create Date: 2024-02-28 15:50:40.429681

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '193415b3b0c3'
down_revision: Union[str, None] = '7615afcfbec4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
