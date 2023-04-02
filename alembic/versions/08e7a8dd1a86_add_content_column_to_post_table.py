"""add content column to post table

Revision ID: 08e7a8dd1a86
Revises: 546457f0d408
Create Date: 2023-04-01 18:49:57.595097

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08e7a8dd1a86'
down_revision = '546457f0d408'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
