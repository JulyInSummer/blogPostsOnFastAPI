"""add foreign-key to posts table

Revision ID: ce923e3f6cf8
Revises: 192c7f1d66e3
Create Date: 2022-06-13 13:55:22.122127

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ce923e3f6cf8'
down_revision = '192c7f1d66e3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key('posts_user_fkey', source_table='posts', referent_table='users', local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('posts_user_fkey', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
