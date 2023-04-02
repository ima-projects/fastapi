"""add foreign key to posts table

Revision ID: 2b16de7b808b
Revises: 67f495dfac96
Create Date: 2023-04-01 21:11:20.487977

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2b16de7b808b'
down_revision = '67f495dfac96'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    #this is just like how you had to drop the table manually in the database by having to drop the constraint (bc delete table wouldn't work)
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
