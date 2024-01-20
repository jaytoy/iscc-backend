"""add product link table

Revision ID: 26b0560859cf
Revises: ed4037eea889
Create Date: 2024-01-20 11:32:23.473312

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '26b0560859cf'
down_revision: Union[str, None] = 'ed4037eea889'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product_color_size_link',
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('color_id', sa.Integer(), nullable=False),
    sa.Column('size_id', sa.Integer(), nullable=False),
    sa.Column('availability', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['color_id'], ['colors.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.ForeignKeyConstraint(['size_id'], ['sizes.id'], ),
    sa.PrimaryKeyConstraint('product_id', 'color_id', 'size_id')
    )
    op.drop_table('product_size_link')
    op.drop_table('product_color_link')
    op.add_column('products', sa.Column('image_url', sa.String(), nullable=True))
    op.drop_index('ix_products_image', table_name='products')
    op.create_index(op.f('ix_products_image_url'), 'products', ['image_url'], unique=False)
    op.drop_column('products', 'image')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('image', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_products_image_url'), table_name='products')
    op.create_index('ix_products_image', 'products', ['image'], unique=False)
    op.drop_column('products', 'image_url')
    op.create_table('product_color_link',
    sa.Column('product_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('color_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('availability', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['color_id'], ['colors.id'], name='product_color_link_color_id_fkey'),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], name='product_color_link_product_id_fkey'),
    sa.PrimaryKeyConstraint('product_id', 'color_id', name='product_color_link_pkey')
    )
    op.create_table('product_size_link',
    sa.Column('product_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('size_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('availability', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], name='product_size_link_product_id_fkey'),
    sa.ForeignKeyConstraint(['size_id'], ['sizes.id'], name='product_size_link_size_id_fkey'),
    sa.PrimaryKeyConstraint('product_id', 'size_id', name='product_size_link_pkey')
    )
    op.drop_table('product_color_size_link')
    # ### end Alembic commands ###