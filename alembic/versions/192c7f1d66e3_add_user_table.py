"""add user table

Revision ID: 192c7f1d66e3
Revises: 98de4471372b
Create Date: 2022-06-13 12:34:44.700464

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '192c7f1d66e3'
down_revision = '98de4471372b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('password', sa.String(), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
