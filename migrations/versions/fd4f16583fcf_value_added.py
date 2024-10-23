"""Value added

Revision ID: fd4f16583fcf
Revises: 9302ebb2541f
Create Date: 2024-10-14 13:24:57.655148

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fd4f16583fcf'
down_revision: Union[str, None] = '9302ebb2541f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
