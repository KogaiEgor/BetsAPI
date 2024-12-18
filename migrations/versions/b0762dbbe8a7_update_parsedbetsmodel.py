"""Update ParsedBetsModel

Revision ID: b0762dbbe8a7
Revises: 5e52f215ddb0
Create Date: 2024-10-31 12:44:01.319269

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b0762dbbe8a7'
down_revision: Union[str, None] = '5e52f215ddb0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ParsedBets', sa.Column('market', sa.String(), nullable=True))
    op.add_column('ParsedBets', sa.Column('odd', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('ParsedBets', 'odd')
    op.drop_column('ParsedBets', 'market')
    # ### end Alembic commands ###
