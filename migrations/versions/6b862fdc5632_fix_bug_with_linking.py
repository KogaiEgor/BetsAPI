"""Fix bug with linking

Revision ID: 6b862fdc5632
Revises: 7b8bbbe25297
Create Date: 2024-09-13 18:05:12.290136

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6b862fdc5632'
down_revision: Union[str, None] = '7b8bbbe25297'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('AllBets', sa.Column('acc_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'AllBets', 'Accounts', ['acc_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'AllBets', type_='foreignkey')
    op.drop_column('AllBets', 'acc_id')
    # ### end Alembic commands ###
