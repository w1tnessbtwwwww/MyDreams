"""empty message

Revision ID: 9cd8e1b5661a
Revises: e2f0a24afe08
Create Date: 2025-01-12 23:00:22.341003

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9cd8e1b5661a'
down_revision: Union[str, None] = 'e2f0a24afe08'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users_wishes',
    sa.Column('wish_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('wish', sa.String(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('source_url', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('wish_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users_wishes')
    # ### end Alembic commands ###
