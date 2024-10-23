"""BetModel update Del arbs table

Revision ID: 88ffaeea65cc
Revises: 6e7dd269eee1
Create Date: 2024-04-25 15:35:24.692257

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '88ffaeea65cc'
down_revision: Union[str, None] = '6e7dd269eee1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Arbs')
    op.add_column('Bets', sa.Column('bk2_koef', sa.Float(), nullable=True))
    op.add_column('Bets', sa.Column('arb', sa.Float(), nullable=True))
    op.drop_column('Bets', 'bet_on')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Bets', sa.Column('bet_on', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('Bets', 'arb')
    op.drop_column('Bets', 'bk2_koef')
    op.create_table('Arbs',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"Arbs_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('bk1_koef', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('bk1_pre_koef', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('bk2_koef', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('arb', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('bet_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['bet_id'], ['Bets.id'], name='Arbs_bet_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='Arbs_pkey')
    )
    # ### end Alembic commands ###
