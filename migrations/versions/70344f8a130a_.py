"""empty message

Revision ID: 70344f8a130a
Revises: bc15ea73183a
Create Date: 2023-10-22 17:03:26.442476

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70344f8a130a'
down_revision = 'bc15ea73183a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('shopping_cart_item')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shopping_cart_item',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('product_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], name='shopping_cart_item_product_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='shopping_cart_item_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='shopping_cart_item_pkey')
    )
    # ### end Alembic commands ###
