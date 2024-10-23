"""Add name to Bets

Revision ID: 858a05836351
Revises: 88ffaeea65cc
Create Date: 2024-04-25 15:39:32.172393

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '858a05836351'
down_revision: Union[str, None] = '88ffaeea65cc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Bets', sa.Column('name', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Bets', 'name')
    # ### end Alembic commands ###
