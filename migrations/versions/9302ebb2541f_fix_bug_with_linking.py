"""Fix bug with linking

Revision ID: 9302ebb2541f
Revises: 6b862fdc5632
Create Date: 2024-09-13 18:05:43.244909

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9302ebb2541f'
down_revision: Union[str, None] = '6b862fdc5632'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
