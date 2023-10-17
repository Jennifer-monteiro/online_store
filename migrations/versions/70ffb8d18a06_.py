"""empty message

Revision ID: 70ffb8d18a06
Revises: 9db963f240d3
Create Date: 2023-10-17 17:52:32.498962

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70ffb8d18a06'
down_revision = '9db963f240d3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.drop_column('image_path2')
        batch_op.drop_column('image_path1')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('product', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_path1', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('image_path2', sa.VARCHAR(length=255), autoincrement=False, nullable=True))

    # ### end Alembic commands ###
