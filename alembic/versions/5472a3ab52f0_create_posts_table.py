"""create posts table

Revision ID: 5472a3ab52f0
Revises: 
Create Date: 2022-06-13 11:51:33.726496

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5472a3ab52f0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True), 
        sa.Column('title', sa.String(), nullable=False),
        )
    pass

def downgrade() -> None:
    op.drop_table('posts')
    pass
