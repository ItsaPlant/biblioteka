"""empty message

Revision ID: 3a57ac5cd284
Revises: 
Create Date: 2021-10-06 14:48:58.262266

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3a57ac5cd284'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('books', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('author', sa.String(length=200), nullable=True),
    sa.Column('title', sa.String(length=200), nullable=True),
    sa.Column('status', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_book_status'), 'book', ['status'], unique=False)
    op.create_index(op.f('ix_book_title'), 'book', ['title'], unique=False)
    op.create_table('authors',
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['author.id'], ),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.PrimaryKeyConstraint('author_id', 'book_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('authors')
    op.drop_index(op.f('ix_book_title'), table_name='book')
    op.drop_index(op.f('ix_book_status'), table_name='book')
    op.drop_table('book')
    op.drop_table('author')
    # ### end Alembic commands ###