"""add content column for posts table

Revision ID: b7b8912f12dc
Revises: 4fd6f9fd30c8
Create Date: 2025-03-07 12:57:26.236854

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b7b8912f12dc'
down_revision: Union[str, None] = '4fd6f9fd30c8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    pass
