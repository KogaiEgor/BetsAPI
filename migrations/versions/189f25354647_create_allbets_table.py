"""Create AllBets table

Revision ID: 189f25354647
Revises: 858a05836351
Create Date: 2024-09-13 16:54:34.056319

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '189f25354647'
down_revision: Union[str, None] = '858a05836351'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('AllBets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('time', sa.DateTime(), nullable=True),
    sa.Column('market', sa.String(), nullable=True),
    sa.Column('match_name', sa.String(), nullable=True),
    sa.Column('is_placed', sa.Boolean(), nullable=True),
    sa.Column('meta', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('AllBets')
    # ### end Alembic commands ###
