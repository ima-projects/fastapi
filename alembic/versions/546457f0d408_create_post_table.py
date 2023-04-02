"""create post table

Revision ID: 546457f0d408
Revises: 
Create Date: 2023-04-01 18:32:18.890405

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '546457f0d408'
down_revision = None
branch_labels = None
depends_on = None

#creating the table (a set of commands) - handles the changes
def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False))
    pass

#removing the table (a set of commands) - handles rolling back
def downgrade() -> None:
    op.drop_talbe('posts')
    pass
