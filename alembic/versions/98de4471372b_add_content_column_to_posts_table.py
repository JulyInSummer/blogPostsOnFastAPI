"""add content column to posts table

Revision ID: 98de4471372b
Revises: 5472a3ab52f0
Create Date: 2022-06-13 12:01:05.783002

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98de4471372b'
down_revision = '5472a3ab52f0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
