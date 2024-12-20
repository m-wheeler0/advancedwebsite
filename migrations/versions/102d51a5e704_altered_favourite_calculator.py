"""Altered favourite calculator

Revision ID: 102d51a5e704
Revises: 4bc053fd0921
Create Date: 2024-12-03 04:45:18.288713

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '102d51a5e704'
down_revision = '4bc053fd0921'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('game', schema=None) as batch_op:
        batch_op.drop_column('favourites_count')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('game', schema=None) as batch_op:
        batch_op.add_column(sa.Column('favourites_count', sa.INTEGER(), nullable=True))

    # ### end Alembic commands ###
