"""empty message

Revision ID: 4bc053fd0921
Revises: 71c9888d2024
Create Date: 2024-12-02 18:55:45.789139

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4bc053fd0921'
down_revision = '71c9888d2024'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('email')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.VARCHAR(length=50), nullable=True))

    # ### end Alembic commands ###
